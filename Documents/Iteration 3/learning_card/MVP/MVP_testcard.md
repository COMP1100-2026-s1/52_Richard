
# SkillPath — MVP Test Cards

This document contains test cards for all hypotheses relevant to the SkillPath MVP, organised into three groups: old hypotheses (including those that were refuted or refined), the refined problem hypothesis, and new MVP-feature hypotheses. Each test card records the hypothesis, the test conducted, the metrics used, the success criteria, the evidence collected, the result, and the decision made.

---

## TC-OLD-1: Convenience-Driven Course Selection (Original Problem Hypothesis)

### Hypothesis

We believe that university students primarily select courses based on convenience factors — timetable fit, perceived difficulty, and peer recommendations — rather than based on the skills they want to develop.

### Test

We conducted 5–10 user interviews per team member with university students in Iteration 1, exploring how students currently make course decisions and whether they experience a gap between their course choices and skill awareness.

### Metrics

- Percentage of students whose course choices are primarily driven by convenience.
- Percentage of students who admit they do not know what skills a course develops before enrolling.
- Percentage of students who express frustration or regret about past course choices.

### Criteria

We considered this hypothesis validated if:
- 70%+ of students admit convenience is the primary driver of their course choices.
- 60%+ cannot clearly articulate the skills developed in their courses.
- 50%+ express frustration or regret about past selections.

### Evidence

Iteration 1 interviews (25+ interviews across five team members) showed that convenience was a real factor but not the complete explanation. Students also described a lack of clear, practical information about what courses actually taught. Most students admitted they could not easily list skills from completed courses. Several expressed regret specifically because they chose courses without knowing what they would gain from them.

### Result

**Partially refuted / refined.**
Convenience appeared across interviews but was not the primary driver for all students. The stronger and more consistent finding was that students lacked accessible, specific information about course skills, career relevance, and prerequisites — not simply that they were lazy in their decisions. The hypothesis was refined rather than fully accepted or rejected.

### Decision

Refined the hypothesis. The problem to solve is not convenience-driven selection per se, but the absence of clear, skill-level course information that would allow students to make informed choices even when they wanted to. All subsequent hypotheses and features were grounded in this refined framing.

---

## TC-REFINED-1: Students Lack Clear Skill and Career Information (Refined Problem Hypothesis)

### Hypothesis

We believe that university students lack clear and practical information about the specific skills a course develops, its prerequisites, its career relevance, its workload, and how it connects to future courses or pathways. We believe this information gap — not convenience — is the primary reason students make course choices they later regret or cannot explain to employers.

### Test

We conducted Iteration 2 pre-prototype interviews (3–5 per team member) to explore what information students currently use when selecting courses, what information they wish they had, and whether they could explain the skills developed in courses they had already completed.

### Metrics

- Percentage of students who describe current course information (profile pages, handbook) as insufficient or difficult to interpret.
- Percentage of students who cannot explain what skills a completed course developed.
- Percentage of students who say they would change a past course choice if they had had better skill and career information.

### Criteria

We considered this hypothesis validated if:
- 70%+ describe current information sources as insufficient.
- 60%+ cannot clearly explain skills from a completed course.
- 50%+ say better information would have changed at least one past course decision.

### Evidence

Iteration 2 pre-prototype interviews confirmed the refined problem across all five team members. Students described piecing together information from course profile pages, Reddit, and asking friends. Multiple students said they had no clear idea what skills they were developing until after completing a course. Several said their degree felt directionless because they could not see how courses connected to careers.

### Result

**Accepted.**
The refined problem hypothesis was validated. The information gap — not laziness or convenience — is the primary problem. Students want skill-level clarity, career relevance, and prerequisite visibility before enrolling.

### Decision

Proceeded with developing SkillPath as a course-to-skill-to-career mapping tool. All eight MVP features were designed to address this specific information gap, not the original convenience framing.

---

## TC-MVP-1: Course Detail Card Provides Decision-Useful Information

### Hypothesis

We believe that a redesigned course card explicitly listing 3–5 specific skills, assessment type, difficulty, workload, peer rating, prerequisites, and career-relevant outcomes will help students make more informed course decisions than the current UQ course profile page.

### Test

We built a prototype course card and tested it in Iteration 2 post-prototype interviews across 13 interviewees using a standardised seven-task evaluation. Task 3 asked interviewees to review a course card and identify skills and career outcomes.

### Metrics

- Percentage of interviewees who can identify 3+ skills from the card without prompting.
- Percentage of interviewees who describe the card as clearer or more useful than current UQ course pages.
- Specific feedback on elements that add or reduce clarity.

### Criteria

We considered this hypothesis validated if:
- 80%+ of interviewees can identify 3+ skills from the card without help.
- 70%+ describe the card as more useful than current UQ course information.

### Evidence

All 13 prototype interviewees could identify skills and career outcomes from the course card. The card format was well received overall. Specific feedback identified four issues: skill labels were too vague for students new to a field; assessment type needed to specify format (essay, exam, group work), not just count; difficulty labels ("medium", "hard") were too general; and the card felt visually dense. At least one interviewee described SkillPath as combining UQ's course planner, course profile pages, and peer review platforms into one.

### Result

**Accepted with refinements required.**
The course card concept is validated. Students can extract decision-useful information from it. The implementation requires: brief descriptions or examples added to skill labels, explicit assessment format, clarification of what difficulty means in practice, and reduced visual density.

### Decision

Proceeded with the course detail card as a core MVP feature. Refinements applied in the MVP build: assessment type is now shown as a specific field, skills are categorised, and prerequisites are displayed prominently above skills and career outcomes.

---

## TC-MVP-2: Side-by-Side Course Comparison Reduces Choice Paralysis

### Hypothesis

We believe that students experience confusion and choice paralysis when selecting between similar-sounding courses. A side-by-side comparison tool explicitly showing shared skills, skills unique to each course, workload, peer rating, and prerequisites will reduce that confusion and help students make a confident choice.

### Test

We included course comparison as one of the seven tasks in the Iteration 2 post-prototype evaluation. All 13 interviewees attempted Task 5 (compare two courses). We also ran Feature Test Card 2 in pre-prototype Iteration 2 interviews.

### Metrics

- Percentage of interviewees who successfully complete the comparison task without prompting.
- Whether interviewees describe the comparison information as useful.
- Specific UX issues that prevent task completion.

### Criteria

We considered this hypothesis validated if:
- 70%+ of interviewees find the comparison information useful.
- The concept (not just the implementation) is endorsed by a majority of interviewees.

### Evidence

All 13 post-prototype interviewees encountered the comparison feature. The information shown — skills side by side, workload, peer ratings, prerequisites — was consistently praised across all teams. Multiple interviewees independently named course comparison as the most useful thing SkillPath offers. However, the prototype flow had four simultaneous UX failures: the compare button blended into the background colour; there was no confirmation after selecting the first course; selecting a second course required navigating away and back; there was no way to remove a course without restarting. Multiple interviewees from different teams independently described the flow as confusing or "dumb."

### Result

**Concept accepted; prototype flow rejected.**
The value proposition for course comparison is validated. Students want this feature. The Iteration 2 prototype implementation is not suitable for the MVP and must be rebuilt rather than patched.

### Decision

Rebuilt the course comparison flow end-to-end for the MVP. The session-based comparison list now provides clear feedback when a course is added or removed, and removal does not require restarting the process. The compare button is visually distinct from the background.

---

## TC-MVP-3: Semester Plan Feature Helps Students Organise Course Choices

### Hypothesis

We believe that students planning their next enrolment would benefit from a personal course save list — a place to collect courses they are considering and review them as a group before making a final decision.

### Test

The save-courses feature was present in the Iteration 2 prototype but was not a formal evaluation task. We tracked whether interviewees noticed and commented on it without prompting during the post-prototype sessions.

### Metrics

- Number of interviewees who raise the save/plan feature without being prompted.
- Whether the feature is described as useful for actual enrolment planning.
- Whether demand is consistent across different interviewers and student backgrounds.

### Criteria

We considered demand strong enough to justify core-feature status if:
- 3+ interviewees raise the feature without prompting.
- The feature is described in concrete terms (e.g., as a wish list or semester planner) by at least two interviewees.

### Evidence

At least four interviewees across three different team members raised the save/plan feature unprompted. One described it as a "wish list" for upcoming enrolment. The pattern appeared across different interviewer styles and student backgrounds (engineering, business, data science). This is a stronger signal than prompted feedback because it emerged from natural interaction with the prototype, not a direct question.

### Result

**Accepted.**
Unprompted demand from multiple interviewees across multiple interview streams confirms that the semester plan feature has genuine utility. The signal is consistent and strong enough to treat this as a core MVP feature.

### Decision

Implemented the semester plan as a full core feature in the MVP. Courses can be saved from any course detail page, and the plan page provides a summary view of all saved courses that feeds directly into the skill tracker.

---

## TC-MVP-4: Course Validation Helps Students Align Courses to Career Goals

### Hypothesis

We believe that students who have a career goal in mind would use a tool that checks how well a specific course matches that goal — showing which required career skills the course develops and which it does not — to make a more informed enrolment decision.

### Test

We included course validation as Task 4 in the Iteration 2 post-prototype evaluation. We also tested this concept in pre-prototype Iteration 2 interviews under Feature Test Card 4.

### Metrics

- Percentage of interviewees who complete the validation task without prompting.
- Whether interviewees find the match score and skill breakdown useful.
- Discoverability of the feature in the interface.

### Criteria

We considered the hypothesis validated if:
- 70%+ of interviewees complete the task and describe the output as useful.
- The concept is endorsed even by interviewees who struggled to find the feature.

### Evidence

Most interviewees completed the validation task. Two initially could not locate the validate feature and needed prompting. After completing the task, interviewees responded positively to seeing which skills matched and which were missing. The match score percentage was described as a clear and useful summary. One interviewee noted that if you cannot take a course because you lack prerequisites, the rest of the information is irrelevant — confirming that prerequisite display is a prerequisite (in both senses) to the rest of the card being useful.

### Result

**Accepted with a discoverability issue noted.**
The course validation concept is validated. The implementation needs to be more discoverable — it should not require prompting to find.

### Decision

In the MVP, the validate feature is placed in the main navigation bar and linked from the course detail page. The match score and skill breakdown are the primary output of the validate view.

---

## TC-MVP-5: Skill Tracker Helps Students Understand and Articulate Skills

### Hypothesis

We believe that students struggle to articulate the skills their courses develop, especially when preparing a CV or discussing their background with employers. A skill tracker that automatically aggregates skills from planned courses and displays them by category and development level will help students see and communicate their skill profile.

### Test

We tested the skill articulation hypothesis in Iteration 1 and Iteration 2 pre-prototype interviews, asking students to list skills they had developed from their degree. We also included the skill tracker in the Iteration 2 prototype and observed how interviewees interacted with it.

### Metrics

- Percentage of interviewees in pre-prototype interviews who struggle to list their own skills on the spot.
- Whether interviewees in post-prototype sessions engage with the skill tracker without prompting.
- Whether interviewees describe the tracker as useful for CVs or career planning.

### Criteria

We considered this hypothesis validated if:
- 60%+ of pre-prototype interviewees cannot easily list their skills.
- Post-prototype interviewees describe the skill tracker as useful in a real context (e.g., CV building, career planning).

### Evidence

Iteration 1 and Iteration 2 pre-prototype interviews consistently showed that students struggled to articulate their skills, even for courses they had recently completed. In post-prototype sessions, at least one interviewee (Kd, Jordan's Interview 6) engaged with the skill tracker without prompting and asked how skill levels were determined — indicating genuine interest in the feature's logic. Feature Test Card 5 (Iteration 2) confirmed the hypothesis was accepted across interview streams.

### Result

**Accepted.**
The skill articulation problem is real and consistent across iterations. The skill tracker addresses a genuine need.

### Decision

Implemented in the MVP as an automatic output of the semester plan. Saving courses updates the skill tracker without any additional steps from the student. Skills are grouped by category and assigned a level (Developing, Intermediate, Advanced) based on how many saved courses reinforce each skill.

---

## TC-MVP-6 (NEW): AI Course Advisor Adds Value Over Manual Browsing

### Hypothesis

We believe that some students — particularly those who are uncertain about what to study or who prefer conversational interfaces — will find it faster and more useful to describe their goals in plain language and receive a tailored course recommendation than to manually browse and filter the course list. We believe an AI advisor powered by a language model can produce relevant, trustworthy recommendations when grounded in the actual SkillPath course and career database.

### Test

We will conduct 3–5 user interviews with university students who are asked to use the AI Advisor feature with a real goal they have (e.g., "I want to work in data analytics" or "I am interested in environmental policy"). We will observe whether the recommendations are relevant to their goal and whether they trust the output enough to act on it.

### Metrics

1. Relevance: Percentage of interviewees who describe the AI-recommended courses as relevant to their stated goal.
2. Trust: Whether interviewees express confidence in the recommendations, or ask how the recommendations were generated.
3. Comparison to browsing: Whether interviewees say the AI Advisor was faster or more useful than browsing courses manually.
4. Adoption intent: Whether interviewees say they would use the AI Advisor in a real enrolment decision.

### Criteria

We will consider this hypothesis validated if:
- 70%+ of interviewees describe the recommended courses as relevant to their goal.
- 60%+ say they would use the AI Advisor as part of a real enrolment decision.
- No interviewee reports that the AI Advisor recommended courses that were clearly wrong or misleading.

### Evidence

Not yet collected. This is a new hypothesis introduced in Iteration 3. One Iteration 2 post-prototype interviewee mentioned an AI-based course advisor unprompted as an optional add-on. No formal test has been conducted.

### Result

**To be determined.** Testing to be conducted in Iteration 3.

### Decision

Pending results. If validated, the AI Advisor will be treated as a core feature. If partially validated, we will explore whether the feature needs better framing (e.g., showing which database courses were considered) to increase trust. If rejected, the feature will be removed or deprioritised.

---

## TC-RISK-1: Trust, Data Quality, and Privacy Are Prerequisites for Adoption

### Hypothesis

We believe that some students will refuse to use or rely on SkillPath unless they trust that the information is accurate and evidence-based, and unless they understand how their personal data is stored and used. We believe that trust is not a nice-to-have polish item but a prerequisite for adoption by privacy-conscious and information-quality-conscious students.

### Test

We observed trust-related responses during post-prototype interviews in Iteration 2 across 13 interviewees. We specifically tracked whether interviewees raised concerns about information quality or data privacy without prompting.

### Metrics

- Whether interviewees raise data privacy concerns without being asked.
- Whether interviewees condition their adoption on information accuracy (e.g., "I would only use this if all UQ courses are in it").
- Whether interviewees question the source or basis of skill labels, difficulty ratings, or peer ratings.

### Criteria

We considered this risk hypothesis confirmed if:
- At least one interviewee raises data privacy without prompting.
- At least one interviewee places an explicit condition on their adoption based on data quality or completeness.
- Multiple interviewees across different interview streams question the basis of skill or rating information.

### Evidence

One interviewee explicitly stated they would not use SkillPath without knowing how their data is encrypted, whether it would be used to train AI, and what the privacy policy says. One interviewee stated they would only use the tool once all UQ courses were in the database. Multiple interviewees asked how skill labels and difficulty ratings were determined. One interviewee noted the "Based on UQ graduate outcomes" label added clutter without adding credibility — they wanted to see the source, not just a vague attribution.

### Result

**Accepted as a key risk.**
Trust, data quality, and privacy are real adoption barriers, not cosmetic concerns. They affect a minority of interviewees directly but are likely held silently by others who did not raise them.

### Decision

Accepted as a product risk that must be addressed before wide deployment. Actions for the next iteration: write a plain-language data handling statement; add source attribution to skill labels and peer ratings; allow the skill tracker to show which courses contribute each skill so students can verify the logic; test whether adding source transparency increases trust among privacy-conscious users.

---

## Hypothesis Status Summary

| Test Card | Hypothesis | Status |
|---|---|---|
| TC-OLD-1 | Students primarily select courses based on convenience | Partially refuted — refined |
| TC-REFINED-1 | Students lack clear skill and career information | Accepted |
| TC-MVP-1 | Course detail card is more useful than current UQ profiles | Accepted with refinements |
| TC-MVP-2 | Side-by-side comparison reduces choice paralysis | Concept accepted; prototype flow rebuilt |
| TC-MVP-3 | Semester plan feature helps students organise course choices | Accepted |
| TC-MVP-4 | Course validation helps students align courses to career goals | Accepted with discoverability fix |
| TC-MVP-5 | Skill tracker helps students understand and articulate skills | Accepted |
| TC-MVP-6 | AI Advisor adds value over manual browsing | To be tested in Iteration 3 |
| TC-RISK-1 | Trust, data quality, and privacy are prerequisites for adoption | Accepted as key risk |

---

## Link to Learning Card

The Combined Learning Card (Post-Prototype Testing, Iteration 2) provides the primary learning evidence for test cards TC-MVP-1 through TC-MVP-5 and TC-RISK-1. Each finding in the learning card maps to one or more test cards in this document as follows:

| Learning Card Finding | Linked Test Card |
|---|---|
| Course comparison concept is right but flow needs rebuilding | TC-MVP-2 |
| No action feedback creates compounding confusion | TC-MVP-1, TC-MVP-2, TC-MVP-3, TC-MVP-4 |
| Skill labels need interpretive support for newcomers | TC-MVP-1 |
| Career pathway page does not communicate personalisation | TC-MVP-4 |
| Prerequisites are a decision gate, not secondary information | TC-MVP-1 |
| Save courses feature has real unprompted demand | TC-MVP-3 |
| Data privacy is a legitimate adoption barrier | TC-RISK-1 |
| Course codes are part of how UQ students identify courses | TC-MVP-1 |
| AI advisor raised as optional add-on | TC-MVP-6 |

