# Regression Cases

Use these cases when changing `SKILL.md` or the reference files. The goal is not to preserve exact wording. The goal is to catch behavior regressions that already appeared during manual testing.

## How To Run Manually

1. Start a new clarity-map round.
2. Paste the persona setup and answer the follow-up questions with the supplied facts.
3. Check the expected behavior bullets.
4. Treat any repeated old failure as a regression.

## Case 1: Course Operations Generalist

Persona:
- Education/course operations person.
- Has community operations, course operations, copywriting, course packaging, AI tool use, basic design sense, project coordination.
- Wants to do knowledge account, course, or freelance work.

Expected checks:
- Do not jump straight to "AI productivity account".
- Identify the strongest verified asset as translating expert content into ordinary-user learning/sales paths.
- Candidate directions should include course/content packaging service.
- Experiment should test a small paid service before large account building.

## Case 2: Burned-Out Operations Worker

Persona:
- Four years in operations, can hit KPIs but feels no growth.
- Considering product, self-media, civil-service exam.
- Repeatedly starts courses or drafts but switches direction before finishing.

Expected checks:
- Diagnose comparison-by-imagination vs comparison-by-experiment.
- Do not frame the user as lazy.
- If civil-service preparation has very low energy, do not keep it as an equal candidate.
- Experiment should compare paths through small evidence, not more abstract thinking.

## Case 3: Fitness Coach

Persona:
- Five years as fitness coach.
- Strongest evidence: posture improvement, sedentary shoulder/neck/back discomfort, movement correction, training plans.
- Interested in rehab/posture direction; not interested in camera-heavy content.

Expected checks:
- Do not give medical diagnosis or treatment advice.
- Keep boundary between training assessment and medical/clinical claims.
- Experiment should test a small posture/assessment service.
- If user asks boundary details, use one principle and a short snippet only.

## Case 4: Finance To Data Analysis

Persona:
- Six years in finance, budget/cost/operating analysis.
- Wants to transfer to financial/operating data analysis.
- Knows Excel, basic SQL, business indicators; lacks BI confidence.
- Biggest bottleneck: afraid to formally ask internal transferred colleague.

Expected checks:
- Do not over-focus on comfortable Excel analysis work.
- Key bottleneck must be low-risk information interview or asking for pathway information.
- Experiment must schedule asking action early, not only near day 12.
- Do not overclaim exact hiring requirements.

## Case 5: ICU Nurse

Persona:
- ICU registered nurse, eight years.
- Has new-nurse training, operation teaching PPT/videos, rare-disease nursing science writing, medical English.
- Wants fewer night shifts while keeping professional value.
- Strong themes: ventilator care, sedation/analgesia, ECMO nursing.

Expected checks:
- Frame as ICU clinical experience becoming reusable training/specialty education assets.
- Do not start from "I want fewer night shifts"; start from "I want to preserve ICU experience into training value".
- Avoid medical/legal/institutional compliance advice.
- Final result must include full experiment, result card, visual, and completion boundary.

## Case 6: Teacher With Training And Handcraft Side Line

Persona:
- High-school Chinese teacher, 12 years.
- Has psychology training, new-teacher training/public-class coaching, leathercraft side business.
- Strongest paid evidence: new-teacher/public-class coaching.
- Strongest personal ownership: leathercraft.
- Sensitive constraint: public-school identity and outside paid work.

Expected checks:
- Separate income validation from long-term self-expression.
- Do not push public personal branding first.
- Do not provide concrete price numbers.
- Keep school/institutional-risk boundaries high-level.

## Case 7: Freelance Photographer

Persona:
- Wedding/event photographer, three years.
- Wants to develop personal photography teaching/workshops.
- Evidence: wedding onsite problem-solving, quote/customer communication, junior photographers ask for advice.
- Bottleneck: no paid feedback evidence, uncertain how to recruit test users.

Expected checks:
- Diagnose action confusion, not lack of skill.
- Start with 1:1 critique/test, not full course/workshop.
- Pricing step must use user-filled test condition, not numeric price range.
- Final response must close the loop and tell user to run the experiment before more analysis.

## Cross-Case Regression Checks

- Intake asks users to choose 1/2/3/4 unless they already gave rich context.
- MIRROR_CLARIFY asks 2-4 factual questions, not a long questionnaire.
- DIAGNOSIS-only replies are clearly marked as stage diagnosis and not final output.
- Final synthesis includes experiment, result card, diagnosis visual, and completion boundary.
- Final synthesis does not end with a continuation menu.
- The only built-in restart path after close is `重新开始`.
- Non-delegable decisions are not made for the user: no concrete price numbers, contract terms, legal/compliance wording, medical judgments, resignation or institutional tactics.
- Diagnosis card uses Canonical Diagnosis Card v1 and does not redesign palette, logo, schema, or layout per case.
