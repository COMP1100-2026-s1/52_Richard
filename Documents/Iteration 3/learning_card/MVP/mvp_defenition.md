
# SkillPath — MVP Definition

## What is the MVP?

SkillPath's Minimum Viable Product is a working web application that allows university students to explore courses through the lens of skills and career outcomes, compare options side by side, save a semester plan, and receive personalised recommendations. The MVP is built in Django and deployed locally with a seeded course, skill, and career database.

The MVP is not a polished product. It is the smallest set of features that, taken together, allows us to test whether SkillPath delivers real value to students making course decisions — before we invest further in scale or polish.

---

## MVP Features

### Feature 1 — Course Browser with Skill Filtering

**What it does:** Students can browse all available courses and filter the list by skill category to find courses relevant to what they want to learn.

**Evidence that motivated it:**
Iteration 1 interviews established that students do not have a clear way to search for courses by the skills they will develop. Students described using fragmented sources — course profile pages, Reddit, peers — to piece together what a course actually teaches. Iteration 2 pre-prototype interviews confirmed that all interviewees wanted a single place to find courses by skill or career relevance. Feature Test Card 1 (Iteration 2) found that 80%+ of students agreed a skill-focused course card would be clearer than existing university profiles.

---

### Feature 2 — Course Detail Card

**What it does:** Each course has a dedicated detail page showing its code, name, description, difficulty level, workload, assessment type, peer rating, the specific skills it develops (with categories), prerequisite courses, courses it unlocks, and related courses sharing similar skills.

**Evidence that motivated it:**
Iteration 1 interviews showed that students felt course profile pages were vague and filled with academic language. Feature Test Card 1 (Iteration 2) directly tested whether a redesigned course card listing specific skills and career-relevant outcomes would be more useful than current university course pages — the hypothesis was accepted. Post-prototype interviews (13 interviewees) confirmed that interviewees could identify 3–5 skills and career outcomes from the card without help. Specific feedback was used to refine the card: prerequisites were moved higher in the layout, assessment type was made explicit, and skill descriptions were added to provide interpretive context for students unfamiliar with a field.

---

### Feature 3 — Side-by-Side Course Comparison

**What it does:** Students can select up to two courses and view them side by side, with the interface explicitly showing shared skills (both courses develop), skills unique to the first course, and skills unique to the second course.

**Evidence that motivated it:**
Feature Test Card 2 (Iteration 2) found that 70%+ of students recalled struggling to choose between similar-sounding electives and that 70%+ said a direct comparison UI highlighting skills and careers would be highly valuable. Post-prototype testing (13 interviewees) confirmed that course comparison was named most often as the single most useful thing SkillPath offers. The prototype comparison flow had severe UX problems: the compare button blended into the background, there was no feedback after selecting a course, and removing a course required restarting the entire process. The MVP rebuilt the flow end-to-end so that selection feedback is visible and courses can be removed without restarting.

---

### Feature 4 — Semester Plan (Save Courses)

**What it does:** Students can save courses to a personal semester plan from any course detail page. The plan page shows all saved courses together so students can review their intended enrolment at a glance.

**Evidence that motivated it:**
The save-courses feature was visible in the Iteration 2 prototype but was not one of the seven formal evaluation tasks. Despite this, at least four interviewees across three different team members raised it unprompted — describing it as a "wish list" or semester planner they would use before enrolment. Because the demand emerged without prompting and across different interviewer styles, it was treated as a signal for a core feature rather than an optional extra. The post-prototype learning card (Iteration 3) explicitly listed the Semester Plan as a feature to design and test in the next prototype.

---

### Feature 5 — Course Validation (Career Match)

**What it does:** Students select a course and a target career, and the tool computes a percentage match score. It shows which skills the course develops that are relevant to the career, and which career-required skills the course does not cover.

**Evidence that motivated it:**
Iteration 1 and Iteration 2 interviews showed that students could not articulate how individual courses connected to their career goals. Feature Test Card 4 (Iteration 2) tested whether students would use a tool to check whether a specific course aligned with their intended career path — the hypothesis was accepted. Post-prototype interviews confirmed that users understood the validate feature once they found it, but discoverability was low; two interviewees needed prompting to locate it. The MVP places the validate feature in the main navigation and provides an explicit match score with a breakdown of matched and missing skills.

---

### Feature 6 — Skill Tracker

**What it does:** Based on courses saved in a student's semester plan, the skill tracker automatically aggregates the skills those courses develop. Skills are grouped by category (Data & Analysis, Technical, Research & Communication, Business, Other) and assigned a development level (Developing, Intermediate, Advanced) based on how many planned courses reinforce each skill.

**Evidence that motivated it:**
Iteration 1 interviews found that many students struggled to list the skills their degree had developed, even for courses they had already completed. Feature Test Card 5 (Iteration 2) tested the hypothesis that a skill articulation tool would be valuable for CVs and career planning — the hypothesis was accepted. The skill tracker in the MVP connects directly to the plan feature so that saving a course automatically updates the student's visible skill profile without any extra steps.

---

### Feature 7 — Career Pathway List

**What it does:** A browseable list of career pathways, each showing its required skills and the courses in the database that are relevant to it.

**Evidence that motivated it:**
Iteration 1 interviews showed that students wanted to understand where their courses would lead. Iteration 2 hypotheses confirmed that a course-to-skill-to-career mapping was the core value proposition of SkillPath. The career list provides the destination layer of the mapping, letting students start from a career goal and work backwards to the courses and skills that are relevant.

---

### Feature 8 — AI Course Advisor

**What it does:** Students describe their goal or interest in plain language (e.g., "I want to work in data science" or "I am interested in cybersecurity"). The AI Advisor, powered by the Gemini API, recommends 3–5 specific courses from the SkillPath database and identifies the single best-matching career pathway, with brief explanations for each recommendation.

**Evidence that motivated it:**
One Iteration 2 post-prototype interviewee raised an AI-based course advisor unprompted as an optional add-on that would appeal to students comfortable with AI tools. No prior test card formally tested this hypothesis. The AI Advisor is included because the infrastructure cost is low on top of the existing course and career database, and because the hypothesis that AI personalisation adds value over browsing alone has not yet been tested. This is the one feature in the MVP that requires fresh hypothesis testing.

---

## What the MVP Does Not Include

The following items were raised during prototype testing but are explicitly out of scope for the current MVP:

- **User accounts and persistent login** — all plan and comparison data is stored in the browser session only.
- **Full UQ course database** — the MVP uses a seeded sample dataset. One interviewee stated they would only use SkillPath once all UQ courses were included.
- **Student comments on individual courses** — mentioned by multiple interviewees; not implemented.
- **Colour coding by subject area** — mentioned by two interviewees independently; not implemented.
- **Privacy policy and data handling statement** — one interviewee explicitly raised data privacy as an adoption barrier. This is acknowledged as a risk item for the next iteration.

---

## Summary Table

| Feature | Motivation Source | Status |
|---|---|---|
| Course Browser with Skill Filtering | Iter. 1 interviews; Iter. 2 Feature TC1 | Implemented |
| Course Detail Card | Iter. 1 interviews; Iter. 2 Feature TC1; Post-prototype feedback | Implemented |
| Side-by-Side Course Comparison | Iter. 2 Feature TC2; Post-prototype feedback | Implemented |
| Semester Plan (Save Courses) | Post-prototype unprompted demand (4+ interviewees) | Implemented |
| Course Validation (Career Match) | Iter. 2 Feature TC4; Refined problem hypothesis | Implemented |
| Skill Tracker | Iter. 1 interviews; Iter. 2 Feature TC5 | Implemented |
| Career Pathway List | Iter. 1 interviews; Core value proposition | Implemented |
| AI Course Advisor | Post-prototype suggestion; New untested hypothesis | Implemented (experimental) |

