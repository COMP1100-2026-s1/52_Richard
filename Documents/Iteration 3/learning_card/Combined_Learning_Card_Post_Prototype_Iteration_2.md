# Learning Card — SkillPath Post-Prototype Testing (Iteration 2)

## Hypothesis

We believe that university students often select courses based on convenience factors — timetable fit, perceived difficulty, or peer recommendations — rather than based on the skills they want to develop. We proposed that a tool mapping courses to skills and career outcomes would help students make more intentional choices. In Iteration 2, we built a working prototype of SkillPath and tested it with 13 university students across seven structured tasks to find out whether the prototype clearly communicates this value and whether users can navigate its core features without confusion.

---

## Observations

Post-prototype interviews were conducted across five team members: Brian (2 interviews), Eddie (2), Jordan (2), Pranusha (5), and William (2), for a total of 13 interviewees. Each interview followed a standardised seven-task evaluation form covering homepage navigation, search, course card review, course validation, course comparison, future pathway understanding, and overall usefulness. Interviewees were drawn from UQ and QUT, with backgrounds including engineering, business, data science, and cyber security.

### Overall Reception

All 13 interviewees (100%) said they would use SkillPath before selecting courses, and the majority said they would use it every semester. Multiple interviewees independently compared SkillPath favourably to UQ's existing tools. One described SkillPath as merging three things they currently use separately: UQ's course planner, course profile pages, and external peer review platforms. Another said that, compared to UQ's engineering planning system, "this is one website, not thirty." No interviewee questioned whether the tool was worth building.

### Task 1 — Choose a Starting Path

Most interviewees chose a path from the homepage without significant difficulty. However, several were initially unsure which of the two options (Explore or Validate) to select, and at least one interviewee did not see the side navigation bar at first and thought everything was on a single page. The two-option split was questioned by more than one interviewee — one asked whether there would be more options in the final product, another needed clarification before making a choice.

### Task 2 — Search by Skill or Career

This was the task that received the most consistently positive responses. Most interviewees described the search as very easy or intuitive and completed it quickly. Two interviewees across different teams independently noted that the back button within the search interface was too small and easy to miss. One interviewee also noted that search results were limited, though they acknowledged this was a prototype constraint.

### Task 3 — Review a Course Card

Interviewees were generally able to identify three to five skills and potential career outcomes from a course card without help. The overall format of the card was well received. Specific feedback included:

- Skill labels were sometimes too vague. Interviewees who were new to a subject area could see the label (e.g., "exploratory data analysis") but did not know what it meant in practice. Skills need brief descriptions or worked examples, not just names.
- Assessment type should be specified. One interviewee noted that a label like "developed across three assessments" does not tell you whether those assessments are essays, group projects, or exams. This matters when choosing a course.
- Difficulty labels ("medium," "high") were too general. At least one interviewee noted that these categories mean different things to different people and asked for specifics on what makes a course harder or easier for most students.
- "All Skills at a Glance" was described as redundant by one interviewee, since the full skills list is displayed directly next to it. The summary does not add anything the card has not already shown.
- The note "Based on UQ graduate outcomes" was described as adding clutter without adding information — one interviewee suggested just writing the outcome directly without attributing it.
- The card felt visually dense to at least one interviewee, who described it as "too crowded."

### Task 4 — Validate a Course Choice

Most interviewees completed this task. Two initially could not find the validate feature and needed prompting to locate it. One interviewee noted that after adding a course to their plan, there was no visible confirmation that the action had worked — they were left unsure whether the course had been saved.

### Task 5 — Compare Two Courses

This was the most consistently problematic task across all 13 interviews. Specific issues reported:

- The compare button blended into the background colour and was hard to spot on first encounter. Multiple interviewees across different teams mentioned this independently.
- After selecting the first course for comparison, there was no visible confirmation that the course had been queued. Multiple interviewees did not realise the course was already selected and navigated away or repeated the action.
- Selecting a second course required navigating back to the course browser, which felt disconnected from the comparison screen. One interviewee described the flow as "kind of dumb."
- There was no way to remove or swap a course from the comparison without restarting the entire process. One interviewee described going through the course browser again just to unselect a course as "redundant."
- The career match indicator was too small and displayed in the same colour as the surrounding text, making it easy to overlook.

Despite all of this, the information shown in the comparison view — skills side by side, workload, peer ratings, prerequisites — was consistently praised. Multiple interviewees across different teams independently named course comparison as the most useful thing SkillPath offers. The concept is validated; the implementation is not.

### Task 6 — Understand Future Pathways

Experiences here varied more than for any other task. Some interviewees found the feature immediately useful and clear; others were confused for specific reasons:

- At least one interviewee thought the career pathway page was a generic, static reference for all students, not a personalised view based on their own courses and skills. The page does not make clear whose pathway it is showing.
- One interviewee was confused about why prerequisite and pathway information was located in a different tab than they expected, and said they would have liked a set of instructions to guide the first visit.
- One interviewee raised the point that prerequisites should be displayed more prominently than skills and career outcomes — if a student is not eligible to take a course, the rest of the course information is irrelevant to them.

### Task 7 — Overall Usefulness

All 13 interviewees said they would use SkillPath before selecting courses. The most common reasons given were: it consolidates information that is currently spread across multiple sources, it provides skill-level clarity that course profile pages do not offer, and it makes comparing options practical rather than requiring manual side-by-side research. Two caveats were recorded:

- One interviewee said they would use it only once all UQ courses were in the database, not just the current prototype set.
- One interviewee (a cyber security student) said they would not use the app until they knew how their personal data was encrypted, whether it would be used to train AI models, and what the privacy policy covers.

### Features Mentioned Without Prompting

The following features were raised by interviewees without being prompted by any formal task. Because they emerged spontaneously across different interviews and different interviewers, they carry more weight than responses to direct questions.

- **Save Courses / Semester Planner.** Mentioned by at least four interviewees across three different team members. Users wanted to save courses to a plan and view that plan as an organised semester layout — one described it as a "wish list" for upcoming enrolment. This feature was visible in the prototype but was not one of the seven formal tasks.
- **Previous student comments on individual courses**, beyond the numerical peer rating already shown.
- **Colour coding by subject or discipline**, to reduce visual monotony and help users scan faster.
- **More images and fewer text blocks**, raised by two interviewees independently.
- **A readiness or preparedness indicator**, so the app could tell a student whether they have the background to take a course comfortably.
- **Course popularity tracking**, such as what courses other students are taking this semester or took last semester.
- **An AI-based course advisor**, raised by one interviewee as an optional add-on that would appeal to students comfortable with AI tools.

---

## Learning Insights

The prototype testing round confirmed that the product concept is sound. No interviewee questioned whether a tool like SkillPath was worth having. The learning from this round is about where the prototype works, where it does not, and what users want that the current design does not yet address.

**The course comparison concept is the right feature, but the current flow needs to be rebuilt, not adjusted.**
The comparison feature was named most often as both the most useful and the most confusing aspect of the prototype. This is not a contradiction — the information in the comparison view is what users want, but the process of getting to that view is broken in several places at once (no selection feedback, back-and-forth navigation, no way to modify choices, invisible controls). Fixing individual elements one at a time will not be enough; the entire flow needs to be redesigned together.

**No feedback after a user action creates confusion that multiplies.**
A clear pattern across multiple tasks was that users took an action — adding a course to compare, adding a course to their plan, choosing a path — and received no visible response from the interface. Without any confirmation, they repeated steps, lost confidence, or assumed the action had not worked. This is a straightforward fix but it affected nearly every task in the evaluation.

**Skills listed on the course card need interpretive support for students new to a subject.**
Users who were already familiar with a field could read a skill label and immediately understand it. Users who were new could not. A brief description of what each skill means in the context of that course, or an example of when and how that skill gets used, would make the card useful to a much wider range of students — which is exactly the audience SkillPath is targeting.

**The career pathway page does not communicate that it is personalised.**
At least one interviewee thought the career pathway page was a general reference view, not one tailored to their specific courses and skills. If users think the page is generic, they will not trust its recommendations. The page needs to make clear at a glance that it is responding to their data, not showing a default pathway for everyone.

**Prerequisites are a decision gate, not a secondary piece of information.**
One interviewee pointed out that if you cannot take a course because you have not completed the prerequisites, everything else on that course card is irrelevant. Prerequisites should appear at or near the top of the course card, before skills and career outcomes, not at equal visual weight alongside them.

**SkillPath is already understood by users as a consolidation tool, and that creates a high bar.**
One interviewee described SkillPath as combining UQ's course planner, course profile pages, and peer review platforms into one. This framing is encouraging, but it also means users will expect each of those three components to be at least as good as the individual tools they currently use. A weak peer review section, for example, will send users back to whatever platform they used before.

**The "save courses / plan" feature has real demand that did not need to be prompted.**
Across multiple interviews run by different team members, users noticed the save feature and immediately imagined using it as a semester planner or wish list. This happened without prompting and across different interviewer styles, which is a stronger signal than prompted feedback. The feature should be treated as a core part of the next prototype, not an optional extra.

**The tool's value is highest at decision-heavy points in a degree, not necessarily every enrolment.**
One interviewee said she would use SkillPath specifically for electives, not mandatory core courses. Another said it would have been most useful when choosing a minor. This suggests the highest-value use case is not routine enrolment but specific moments of choice — when students have options and no clear way to evaluate them. Understanding this might shape how the product is marketed and introduced.

**Data privacy is a legitimate adoption barrier for some users.**
One interviewee explicitly said they would not use SkillPath without knowing how their data is encrypted, stored, and whether it would be used to train AI. This was one person, but the question is reasonable and likely held silently by others who did not raise it. Privacy-conscious users need a clear statement about data handling before they will sign in or share course information.

**Course codes are part of how UQ students identify and categorise courses.**
One interviewee noted that UQ students routinely refer to courses by code (e.g., STAT7701), not by full title, and that the course code also signals the course level immediately — a 7000-level code tells you it is a postgraduate course before you read anything else. Removing codes to look cleaner may create friction for the exact users the tool is built for. This deserves direct testing.

---

## Future Action

We will proceed with SkillPath and treat the post-prototype interviews as confirming the product concept. In the next iteration, we will investigate and address the following:

- Redesign the course comparison flow end-to-end, so that: selecting a course for comparison provides visible confirmation; both courses can be chosen from the same screen without back-and-forth navigation; a selected course can be swapped or removed without restarting; the career match indicator is clearly visible and distinct from surrounding elements.
- Add visible feedback for every user action that saves or updates something — adding a course to compare, adding a course to a plan, and choosing a starting path.
- Add brief descriptions or concrete examples to each skill label on the course card, especially for fields where skill names are not self-explanatory to newcomers.
- Move prerequisite information higher on the course card, so it appears before skills and career outcomes rather than alongside them.
- Redesign the career pathway page to make clear at a glance that the pathway shown is specific to the logged-in student's courses and goals, not a generic reference.
- Test course card layouts with and without course codes included in the title, to determine which format students find more useful and familiar.
- Design and test a basic "Save Courses / Semester Plan" view, treating this as a core feature given the strength of unprompted demand across multiple interviews.
- Write a brief, plain-language summary of how student data is stored and used, and determine where in the product this should appear.
- Increase visual contrast throughout the interface and reduce text density on the course card, incorporating images or icons where they replace rather than accompany long text blocks.
