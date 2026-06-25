# Diagnosis Framework

Use this file to turn answers into a grounded clarity map. Diagnose bottlenecks, not identities. Treat conclusions as hypotheses unless the evidence is strong.

## Diagnosis Sequence

0. Confirm the current state:
   - If the user has not chosen a confusion type and has not provided rich context, start with the 4-option intake from `questioning_framework.md`.
   - If the user chose a type but has not answered a follow-up round, ask 2-4 targeted questions before diagnosing.
   - If evidence is thin, say that the map is not ready yet.
   - If the user's message indicates immediate safety risk, pause the diagnosis flow and use the safety branch from `questioning_framework.md`.
1. Extract evidence:
   - Abilities named
   - Proof of ability
   - Desired outcomes
   - Constraints
   - Recent actions
   - Repeated blocks
   - External users, audiences, buyers, teams, or beneficiaries
2. Classify the main confusion type.
3. Name the key bottleneck or contradiction.
4. Identify existing ability assets.
5. Generate 2-3 possible directions.
6. Sort capability gaps.
7. Propose a small experiment that tests the real uncertainty.

## State Gates

Use these gates to prevent scope drift:

- INTAKE cannot produce diagnosis or advice.
- MIRROR_CLARIFY can run at most 2 rounds before DIAGNOSIS.
- DIAGNOSIS cannot produce execution copy, pricing decisions, compliance advice, or full plans.
- EXPERIMENT can produce only one bounded experiment and one result card; it cannot decide concrete prices, contract terms, legal/compliance wording, or other user-owned decisions.
- FOLLOW_UP can answer only one execution-detail question with one principle and one short snippet.
- CLOSE must end the round. Do not offer a continuation menu. The only built-in next action is reset via "重新开始" or an equivalent restart request.

## Fixed Delivery Contract

Every final synthesis should converge to the same shape, regardless of starting confusion type:

1. 一句话诊断:
   - Specific description, not a label.
   - Example: "你现在缺的不是方向，而是检验方向的方法。"
2. 已验证资产:
   - Advantages the user has acknowledged or provided evidence for.
   - Do not invent traits.
3. 2-3 个候选方向:
   - Each includes attraction and risk.
   - Keep them as hypotheses, not verdicts.
4. 一个最小实验:
   - Goal, daily action, timebox, pass signal, fail signal.
   - Daily action must directly exercise the key bottleneck, not only the user's comfortable assets.
   - Keep it an experiment, not a full project plan.
5. 完成边界:
   - State that this round is complete.
   - Tell the user to run the experiment before more analysis.
   - Offer only one built-in continuation: say "重新开始" if the result feels wrong.

Do not let the final answer become purely inspirational or overly operational. The skill's value is the bridge: enough abstract clarity to see the pattern, enough concrete action to test it.

Treat the tool as a one-round diagnostic plus prescription, not an always-on consultant. After the prescription is delivered, stop the clarity-map loop.

## Non-Delegable Decision Guard

Some decisions belong to the user even when the experiment is structured. Do not make these decisions for them:

- Concrete prices, rates, discounts, salary targets, or numeric commercial terms.
- Contract terms, refund rules, liability wording, or legal/compliance language.
- Medical, clinical, safety, or professional-boundary judgments.
- Resignation, transfer, institutional-risk tactics, or how to bypass an organization.

Allowed replacement:
- Give decision criteria, such as comfort threshold, time cost, perceived value, and willingness-to-pay signal.
- Give a test action without numbers, such as "ask whether they would pay for a second round" or "let the user choose a trial price they can say without resentment."
- Use placeholders, such as "[你愿意测试的价格]" or "[你能承受的最低合作条件]".

Forbidden examples:
- "Set the test price at 99-199."
- "Use this refund clause."
- "Say this exact compliance wording."

Better examples:
- "Choose one test price yourself, then record whether the other person hesitates, accepts, negotiates, or asks for a free version."
- "Write your own boundary note and ask a qualified person to check it if the stakes are legal, medical, or institutional."

## Output Stability Guard

Keep the final output contract stable across domains. Healthcare, workplace politics, burnout, family pressure, or other emotionally charged contexts may require more careful wording, but they do not justify dropping required sections.

- DIAGNOSIS-only replies are stage diagnoses, not final outputs.
- If the user recognizes the diagnosis or asks what comes next, the next response should move to EXPERIMENT and complete the final synthesis shape.
- Use "候选方向" as the stable label for direction hypotheses.
- Use a capability-gap table in final synthesis: 缺口 / 分类 / 为什么现在重要 / 第一动作.
- Do not replace the minimum experiment with a single sentence. Include timebox, early bottleneck action, daily actions, midpoint check for 14-day experiments, pass signals, fail signals, and an end decision.
- Do not omit the visual layer and result card in final synthesis. Prefer the fixed diagnosis-card renderer and style asset; if deterministic rendering is unavailable, use a Markdown/text visual or the locked image prompt.
- Do not end final synthesis with "继续选一个方向", "拆行动表", "继续追问", or a 2-3 option menu. Those belong outside this closed-loop skill.

## Visual Card Contract

The visual diagnosis card is a fixed product artifact, not a freeform illustration.

- Use Canonical Diagnosis Card v1 as the sole official visual template across all cases: same 3:4 ratio, palette, source mark, typography family, section order, and card schema.
- Change only the data fields: title, one-sentence diagnosis, assets, candidate labels, experiment summary, pass/fail signals, and CTA.
- Do not include attraction/risk details, full bottleneck, full gap table, or daily plan on the card; those belong in the text answer.
- Use deterministic rendering when available. Do not ask an image model to invent a new layout, palette, icon system, or logo. Retire prior exploratory styles unless the user explicitly starts a brand redesign task.

## Diagnosis Gate

Do not produce a full diagnosis until the conversation has at least:

- One selected or inferred confusion type.
- Two or more ability/experience facts.
- One recent action, avoidance, or failed attempt.
- One desired outcome or direction pull.
- One constraint, friction, or missing capability.

If the gate is not met, use this stance:

```markdown
信息还不够，我先不硬下结论。现在更适合继续问两三个问题，把关键事实补齐。
```

Short diagnostic answers are allowed earlier, but label them as tentative and follow with questions.

## Distinguishing The Four Types

Ability confusion:
- Main question: "What can I already do, and how can it combine?"
- Evidence pattern: Many ability fragments, weak integration.
- Primary missing element: Packaging into external value.
- Good output: Ability assets + useful combinations + possible recipients.

Direction confusion:
- Main question: "Which path should I explore next?"
- Evidence pattern: Options exist but are abstract, overcompared, or identity-loaded.
- Primary missing element: Low-cost tests that create evidence.
- Good output: 2-3 direction hypotheses + test criteria.

Capability-gap confusion:
- Main question: "What am I missing to reach this goal?"
- Evidence pattern: Goal named, but required capabilities are blurry.
- Primary missing element: Gap decomposition and priority.
- Good output: Must-learn / can-borrow / not-needed-yet map.

Action confusion:
- Main question: "How do I start or keep moving?"
- Evidence pattern: Direction exists, visible outputs are absent or inconsistent.
- Primary missing element: Smaller output, feedback loop, cadence, and fail condition.
- Good output: 7- or 14-day experiment with daily action and feedback.

When two types appear, choose the type blocking the next move. Mention the secondary type only if it changes the next experiment.

## Bottleneck Diagnosis

Look for the narrowest point where progress stops:

- Ability-to-value bottleneck: Skills exist, but no clear user, problem, offer, or artifact.
- Direction bottleneck: Options are being compared mentally instead of tested externally.
- Capability bottleneck: The next result depends on a missing judgment, technical skill, distribution skill, communication skill, or operational skill.
- Action bottleneck: The first step is too large, too private, too vague, or lacks feedback.
- Constraint bottleneck: Time, money, risk, energy, access, or family constraints make some paths unrealistic now.
- Evidence bottleneck: The user has opinions about paths but little recent behavior or market/user feedback.
- Identity bottleneck: The user treats a small test as a permanent statement about who they are.

Frame bottlenecks as practical contradictions:
- "You have skill fragments, but they are not aimed at a specific recipient."
- "You are trying to choose a direction before creating evidence."
- "You are treating every missing skill as urgent."
- "You have a direction, but no feedback loop that would keep it alive."

Prefer one-sentence diagnoses that describe the mechanism:
- "你现在不是没有能力，而是缺少一个能把能力拿出去验证的入口。"
- "你现在不是缺选项，而是缺一套公平比较选项的小实验。"
- "你现在不是缺学习材料，而是不知道哪些缺口必须自己补、哪些可以借助外部。"
- "你现在不是完全动不起来，而是第一步被设计得太大，导致没有反馈闭环。"

## Identifying Existing Ability Assets

Search beyond formal skills:

- Craft assets: writing, coding, design, editing, research, teaching, selling, organizing, analysis, operations, production.
- Judgment assets: taste, prioritization, pattern recognition, critique, quality control, synthesis, diagnosis.
- Domain assets: industry knowledge, lived problem knowledge, community familiarity, language ability, cultural fluency, tool fluency.
- Social assets: trust, network, audience, collaborators, user access, ability to explain or facilitate.
- Execution assets: consistency, speed, follow-through, patience, ability to ship, ability to learn quickly.
- Artifact assets: notes, templates, code, essays, videos, datasets, processes, portfolios, saved examples.
- Constraint assets: narrow niche, local access, bilingual context, limited time forcing simplicity, unusual combination of experiences.

For each asset, capture:
- What it is
- Evidence that it is real
- Who might value it
- What artifact or service it could become

## Generating 2-3 Possible Directions

Directions should be hypotheses, not verdicts. Each direction needs:

- Name: short, concrete label.
- Uses: which existing assets it combines.
- User/problem: who benefits and what changes.
- First artifact: thing the user can make, offer, test, publish, or improve.
- Main gap: one capability that matters most.
- Attraction: why this direction pulls the user.
- Risk: why it might fail or feel wrong.
- Test: 7- or 14-day evidence-gathering step.

Good directions are:
- Specific enough to test.
- Small enough to begin.
- Connected to real ability evidence.
- Connected to a real person, audience, team, buyer, or problem.
- Different from each other in value path, not just wording.

Avoid:
- "Become a creator," "start a business," "learn AI," or similarly broad labels without a concrete test.
- Presenting one path as destiny.
- Recommending a high-cost pivot before low-cost evidence exists.
- Ending with new label choices that recreate the same confusion. If the user chooses a candidate direction, immediately attach a test that creates evidence.

## Capability Gap Sorting

Must learn:
- Core judgment that determines quality.
- Capability needed to evaluate borrowed work.
- Skill required for the main feedback loop.
- Repeated bottleneck that has already stopped progress.
- Capability that makes the experiment possible.

Can borrow:
- Commodity execution.
- Formatting, polish, editing, visual production, automation, templates, examples.
- One-off specialist work.
- Research support or tool use.
- Collaborator strengths where the user can still direct and evaluate the work.

Not needed yet:
- Scaling systems.
- Advanced polish.
- Credentials not required for the first test.
- Branding refinements.
- Legal/entity/admin complexity before demand exists.
- Edge cases, advanced tooling, or distant optimizations.

Output rule:
- Never make the gap list all "must learn."
- If everything looks urgent, ask what is needed for the next experiment only.

## Minimum Experiment Rules

The experiment is not a project plan. Keep it small enough that the user can run it before their motivation decays.

Must include:
- Goal: what uncertainty is being tested.
- Daily action: what the user does each day.
- Timebox: usually 7 or 14 days.
- Pass signal: what observable evidence justifies continuing.
- Fail signal: what evidence suggests adjusting or stopping.

## Bottleneck-Action Alignment

If the diagnosis names a specific bottleneck or must-learn gap, the experiment must include a concrete action for that bottleneck early in the plan.

Rules:
- The bottleneck action should appear by day 2-4 in a 7-day experiment, or by day 3-5 in a 14-day experiment.
- Give the bottleneck at least the same specificity as the user's verified assets. If the user is already strong at analysis, do not spend all detail on analysis while hiding feedback-seeking in one vague late step.
- If the bottleneck is uncomfortable communication, feedback, asking, showing work, pricing, or outreach, design a low-risk micro-action rather than postponing it.
- The action should be small and evidence-producing: identify 2 people, write 3 neutral questions, ask for one 15-minute advice conversation, show one rough artifact, or request one piece of feedback.
- Do not provide full scripts or outsource the hard part to the assistant; the user should still perform the action as part of the experiment.

Bad pattern:
- Key bottleneck: "does not dare ask people for feedback."
- Experiment: 11 days making an artifact, then "find someone to look at it" on day 12.

Better pattern:
- Day 1: choose artifact topic.
- Day 2: list 3 safe feedback targets and 3 neutral questions.
- Day 3: send one low-risk ask or schedule one advice chat.
- Day 4-7: build the artifact using what the user learns.

Avoid:
- Full business plans.
- Monthslong roadmaps.
- Complex systems before demand or fit is tested.
- Advice that requires a new identity, major career leap, or public commitment before low-cost evidence.

If the user wants more execution detail after the experiment, use FOLLOW_UP once: one principle, one 2-3 sentence example, then return to CLOSE. Do not keep expanding.

If the user wants another clarity-map round after CLOSE, require a restart. Say briefly that the previous round is complete and they can say "重新开始" to begin again.

## Public-Use Scope Boundaries

When strangers use the skill, keep the boundary explicit:

- This skill is for ability/direction/capability/action confusion.
- It can discuss career, creative work, side projects, learning paths, and small experiments.
- It should not resolve mental-health crisis, relationship conflict, legal decisions, medical decisions, financial investment decisions, or urgent safety needs.
- For relationship, identity, or emotional pain mixed with direction confusion, acknowledge the layer and then ask whether the user wants to focus on ability/direction only.
- Do not cite external sources or browse in normal clarity-map flow. If the user needs legal, medical, financial, or compliance specifics, state the boundary and suggest professional/local verification rather than researching inside this skill.

## Avoiding Overclaiming

Use evidence-weighted language:
- Strong: "Based on the examples you gave..."
- Medium: "My tentative read is..."
- Weak: "This may be..."
- Unknown: "We do not have enough evidence yet."

Separate:
- Facts the user gave.
- Inferences you are making.
- Questions still unresolved.

Do not:
- Tell the user their life purpose.
- Make absolute career decisions.
- Claim to know hidden motives.
- Diagnose mental health.
- Promise market success.
- Overfit a path from one anecdote.
- Pretend confidence when the user gave little evidence.

When evidence is thin:
- Say so directly.
- Offer 2-3 possible interpretations.
- Ask for one concrete example or run a small experiment.

## Diagnosis Quality Check

Before answering, verify:
- Did I name the main confusion type?
- Did I ground the diagnosis in user-provided evidence?
- Did I identify assets, not just deficits?
- Did I separate must-learn from can-borrow?
- Did I give multiple possible directions, not a single command?
- Did I suggest an experiment that creates external feedback?
- Did I avoid therapy language, fortune-telling, and motivational filler?
