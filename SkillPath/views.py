from re import L
import json
import os
import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Skill, Career
from collections import defaultdict, Counter


def index(request):
    return render(
        request,
        "SkillPath/index.html",
        {
            "course_count": Course.objects.count(),
            "skill_count": Skill.objects.count(),
            "career_count": Career.objects.count(),
        },
    )


def course_list(request):
    courses = Course.objects.all()
    return render(request, "SkillPath/course_list.html", {"courses": courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    unlocks = Course.objects.filter(prerequisites=course)
    return render(request, "SkillPath/course_detail.html", {"course": course, "unlocks": unlocks})


def career_list(request):
    careers = Career.objects.all()
    return render(request, "SkillPath/career_list.html", {"careers": careers})


def compare(request):
    # Read the session, if the compare list do not exist, create a empty list, and set it to the compare_list, so clever lehhhhh
    compare_list = request.session.get("compare_list", [])

    # pk__in fetch all courses whose pk is in the list
    courses = Course.objects.filter(pk__in=compare_list)

    shared_skills = []
    first = []
    second = []

    if len(courses) == 2:
        # flat = true returns a flat list, the pk here is the pk of skill
        # The logic here is there is two course in `courses`, and we access each of them and search for the primary key of the skill they develop
        skill = set(courses[0].skills.values_list("pk", flat=True))
        skills = set(courses[1].skills.values_list("pk", flat=True))
        # The skill that both courses will develop
        shared_skills = Skill.objects.filter(pk__in=skill & skills)
        # The skill that first course have while second do not
        first = Skill.objects.filter(pk__in=skill - skills)
        # The skill that second course have while first do not
        second = Skill.objects.filter(pk__in=skills - skill)
    return render(
        request,
        "SkillPath/compare.html",
        {
            "courses": courses,
            "shared_skills": shared_skills,
            "only_first": first,
            "only_second": second,
        },
    )


def compare_add(request, pk):
    # Same, if compare_list do not exist, assign an empty list for it
    compare_list = request.session.get("compare_list", [])
    # This if statement check if the course is not in the list, and the list has fewer than 2 courses, to prevent compare duplicate course and more than 2 course
    if pk not in compare_list and len(compare_list) < 2:
        # Append the course primary key into the list
        compare_list.append(pk)
        # Save the "compare_list"  = the list we just append, manual save
        request.session["compare_list"] = compare_list

    # Send the user back to course after clicking the button
    return redirect("course_list")


def compare_remove(request, pk):
    compare_list = request.session.get("compare_list", [])
    if pk in compare_list:
        compare_list.remove(pk)
        request.session["compare_list"] = compare_list
    # Send the user to compare after clicking the button
    return redirect("compare")


def plan(request):
    saved = request.session.get("saved_courses", [])
    courses = Course.objects.filter(pk__in=saved)
    return render(request, "SkillPath/plan.html", {"courses": courses})


def plan_add(request, pk):
    saved = request.session.get("saved_courses", [])
    if pk not in saved:
        saved.append(pk)
        request.session["saved_courses"] = saved
    return redirect("course_detail", pk=pk)


def plan_remove(request, pk):
    saved = request.session.get("saved_courses", [])
    if pk in saved:
        saved.remove(pk)
        request.session["saved_courses"] = saved
    return redirect("plan")


def validate(request):

    courses = Course.objects.all()
    careers = Career.objects.all()
    context = {"courses": courses, "careers": careers}

    if request.method == "POST":
        course_pk = request.POST.get("course")
        career_pk = request.POST.get("career")
        course = get_object_or_404(Course, pk=course_pk)
        career = get_object_or_404(Career, pk=career_pk)

        course_skills = set(course.skills.values_list("pk", flat=True))
        career_skills = set(career.skills.values_list("pk", flat=True))

        matched = Skill.objects.filter(pk__in=course_skills & career_skills)
        mismatch = Skill.objects.filter(pk__in=career_skills - course_skills)

        match_score = 0
        if career_skills:
            match_score = int(len(matched) / len(career_skills) * 100)

        context.update(
            {
                "selected_course": course,
                "selected_career": career,
                "matched": matched,
                "mismatch": mismatch,
                "match_score": match_score,
            }
        )

    return render(request, "SkillPath/validate.html", context)


def ai_advisor(request):
    recommendation = None
    error = None
    user_goal = ""

    if request.method == "POST":
        user_goal = request.POST.get("goal", "").strip()

        if user_goal:
            courses = Course.objects.prefetch_related("skills").all()
            careers = Career.objects.prefetch_related("skills").all()

            course_data = [
                {
                    "code": c.code,
                    "name": c.name,
                    "difficulty": c.difficulty,
                    "skills": [s.name for s in c.skills.all()],
                }
                for c in courses
            ]

            career_data = [
                {
                    "name": car.name,
                    "description": car.description,
                    "skills": [s.name for s in car.skills.all()],
                }
                for car in careers
            ]

            prompt = f"""You are a course advisor for SkillPath, a UQ course planning tool.
A student has described their goal or interests:

"{user_goal}"

Available courses:
{json.dumps(course_data, indent=2)}

Career pathways and the skills they require:
{json.dumps(career_data, indent=2)}

Recommend the 3 to 5 most relevant courses for this student. Also identify the single best-matching career pathway.

Reply with ONLY valid JSON in this exact format, no extra text:
{{
  "career_match": "<career name from the list>",
  "career_reason": "<one or two sentences explaining why this career fits>",
  "courses": [
    {{"code": "<course code>", "reason": "<one or two sentences explaining why this course fits the student's goal>"}},
    ...
  ]
}}"""

            try:
                from google import genai

                client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt,
                )
                raw = response.text
                json_match = re.search(r"\{.*\}", raw, re.DOTALL)
                if json_match:
                    data = json.loads(json_match.group())
                    recommended_courses = []
                    for item in data.get("courses", []):
                        try:
                            course = Course.objects.prefetch_related("skills").get(
                                code=item["code"]
                            )
                            recommended_courses.append(
                                {"course": course, "reason": item["reason"]}
                            )
                        except Course.DoesNotExist:
                            pass
                    recommendation = {
                        "career_match": data.get("career_match"),
                        "career_reason": data.get("career_reason"),
                        "courses": recommended_courses,
                    }
                else:
                    error = (
                        "The advisor returned an unexpected response. Please try again."
                    )
            except Exception:
                error = "The AI advisor is currently unavailable. Check that GEMINI_API_KEYis set."

    return render(
        request,
        "SkillPath/advisor.html",
        {"recommendation": recommendation, "error": error, "user_goal": user_goal},
    )


def skill_tracker(request):
    saved = request.session.get("saved_courses", [])
    saved_courses = Course.objects.filter(pk__in=saved).prefetch_related("skills")

    skill_counter = Counter()
    for course in saved_courses:
        for skill in course.skills.all():
            skill_counter[skill.pk] += 1

    skills = Skill.objects.filter(pk__in=skill_counter.keys())

    grouped = defaultdict(list)

    for skill in skills:
        count = skill_counter[skill.pk]

        if count >= 4:
            level = "Advanced"

        elif count >= 2:
            level = "Intermediate"

        else:
            level = "Developing"

        progress = min(count * 20, 90)

        grouped[skill.get_category_display()].append(
            {
                "name": skill.name,
                "count": count,
                "level": level,
                "progress": progress,
            }
        )

    categories = [
        {"name": category_name, "skills": skill_list}
        for category_name, skill_list in grouped.items()
    ]

    context = {
        "categories": categories,
        "skill_count": len(skill_counter),
        "course_count": len(saved),
    }

    return render(request, "SkillPath/skill_tracker.html", context)
