# 📋 Product Knowledge Core — Conventions & Standards (`conventions.md`)

This document defines the quality standards, Definition of Ready (DoR), Gherkin Acceptance Criteria rules, and artifact tier selection guidelines that govern all deliverables produced in this workspace.

---

## 🎯 1. Definition of Ready (DoR)

Before any user story can be accepted into a sprint planning session or tagged as `Ready` for engineering, it must satisfy the following checklist:

- [ ] **INVEST Criteria Adherence**:
  - **Independent**: Can be built, tested, and released without hard sequential dependencies on in-progress sprint tickets.
  - **Negotiable**: Details and implementation approaches can be refined during engineering collaboration.
  - **Valuable**: Clear value proposition stated in Concur format (*As a [persona], I want [capability], So that [business benefit]*).
  - **Estimable**: Technical scope is sufficiently bounded so engineering can assign story points ($\le 5$ points).
  - **Small**: Sized to complete within a single sprint iteration (larger stories split via SPIDR).
  - **Testable**: Contains unambiguous, verifiable acceptance criteria.
- [ ] **Gherkin BDD Acceptance Criteria**: Complete `Given/When/Then` scenarios covering happy path, negative path, and boundary conditions.
- [ ] **UI/UX Prototype Linked**: If the feature modifies the user interface, an interactive mockup from `mockups/` or Figma link is attached.
- [ ] **Non-Functional Requirements (NFRs)**: Explicit latency targets, error recovery expectations, and WCAG 2.1 AA accessibility guidelines specified.
- [ ] **Telemetry & Tracking Specified**: Key events, user analytics properties, and outcome metrics defined.
- [ ] **Grooming Readiness Score**: Achieved $\ge 85\%$ when evaluated by `/refine-user-stories`.

---

## 🧪 2. Acceptance Criteria (AC) Rules: Gherkin BDD Standard

All acceptance criteria must be formatted using the Gherkin `Given / When / Then` syntax:

```gherkin
Scenario: [Descriptive Title of the Flow]
  Given [initial context, user authentication state, or system precondition]
  And [additional preconditions if necessary]
  When [the specific user or system action occurs]
  Then [the expected verifiable outcome or state change]
  And [subsequent side effects, e.g., toast notification, database update, or webhook dispatch]
```

### Mandatory Scenario Coverage for Every Story:
1. **Happy Path (Primary Success Flow)**:
   - Valid inputs, nominal system conditions, clear confirmation feedback.
2. **Boundary & Edge Conditions**:
   - Zero-state / empty state handling (e.g., zero search results, first-time user).
   - Maximum input limits (character lengths, file size limits, rate limits).
3. **Negative & Error Handling**:
   - Validation failure (inline field errors, invalid formats).
   - Network failure or service timeout (HTTP 4xx, 5xx graceful degradation).
   - Unauthorized / forbidden access attempt (redirect or friendly permission denial).
4. **Asynchronous & Loading States**:
   - Disabled submit buttons during processing to prevent double-submission.
   - Skeletons, spinners, or progress indicators for actions taking $> 300\text{ms}$.

---

## 📐 3. Template Tier Selection Guidelines

AI PM Sidekick operates across 3 standardized deliverable tiers. Select the appropriate tier in `.context/harness-config.yaml` or pass the `--mode` flag:

| Dimension | ⚡ Lean Mode | 🎯 Standard Agile Mode *(Default)* | 🏢 Enterprise Mode |
| :--- | :--- | :--- | :--- |
| **Target Stage** | Seed startups, MVPs, Hackathons, Rapid spikes | Growth scaleups, Series A–C, Core product sprints | Scale enterprises, Regulated (Fintech, Health), Public cos |
| **PRD Length** | 1 Page (~400–800 words) | 3–5 Pages (~1,500–2,500 words) | 8–15 Pages (~3,500+ words) |
| **User Story Format** | Bulleted functional ACs | Full INVEST format + Gherkin scenarios | INVEST + Gherkin + Traceability Matrix ID |
| **Estimation** | T-Shirt Sizing (S, M, L) | Fibonacci Scale (1, 2, 3, 5, 8) | Story Points + WSJF Cost of Delay |
| **Compliance & Audit** | Basic sanity checks | Standard security best practices | SOC2 Type II, GDPR, Audit logging, SLA/SLO |
| **Sign-Off Flow** | Founder / Solo PM informal approval | PM + Tech Lead + Product Designer sign-off | Formal RACI matrix + Security/Legal review |

### Decision Heuristic:
- Choose **Lean** when the goal is hypothesis testing and learning speed outweighs process overhead.
- Choose **Standard Agile** when building core user-facing features where regression risk and cross-functional handoff require precision.
- Choose **Enterprise** when building multi-tenant infrastructure, billing engines, PII data handling, or compliance-mandated features.

---

## ✅ 4. Definition of Done (DoD)

A story is marked as `Done` when:
- [ ] Code is merged to main branch via approved Pull Request with peer review.
- [ ] Unit and integration test coverage passes without regression.
- [ ] All Gherkin scenarios verified in staging / preview environment.
- [ ] Accessibility (WCAG 2.1 AA) and responsive layouts validated.
- [ ] Associated PRD and technical docs in `docs/` updated to reflect actual release implementation.
- [ ] Jira ticket transitioned to `Released / Done` and release notes logged.

---

## 🔄 5. Operating Model Conventions (`operating_model`)

AI PM Sidekick supports 4 delivery operating models configured via `operating_model` in [`.context/harness-config.yaml`](file:///home/marcin/Documents/Projects/ai-pm-sidekick/.context/harness-config.yaml). Each model shapes how backlogs, cycles, estimation, and handoffs are executed:

| Operating Model | Core Cadence | Unit of Work | Estimation & Sizing | Primary Delivery Gate |
| :--- | :--- | :--- | :--- | :--- |
| **`scrum`** *(Default)* | 1–2 week sprints | INVEST User Stories + Gherkin ACs | Fibonacci story points ($\le 5$ pts) | Definition of Ready ($\ge 85\%$) & Sprint Goal |
| **`shape-up`** | 6-week cycles + 2-week cooldown | Shaped Pitches & Scopes | Fixed Appetite (Small = 1–2 wks, Big = 6 wks) | Betting Table approval & Circuit Breaker |
| **`kanban`** | Continuous pull flow | Backlog items with WIP limits | Cycle time & throughput metrics | WIP column limits & SLA throughput |
| **`gist`** | Iterative experiment loops | Step-projects ($\le 2$ weeks) & Tasks | ICE scoring (Impact, Confidence, Ease) | Metric validation gate to unlock next step |

### Operating Model Selection Heuristics:
1. **Choose `scrum`** when cross-functional engineering sprints require predictable velocity, sprint commitments, and rigorous DoD sign-off.
2. **Choose `shape-up`** when teams suffer from backlog bloat and sprint rollover fatigue, and need bounded appetites with high autonomous design/build agency.
3. **Choose `kanban`** for operational maintenance, ongoing developer platform enhancements, or bug triage queues where work arrives unpredictably.
4. **Choose `gist`** for high-uncertainty 0-to-1 innovation tracks where committing to a multi-month solution is premature before smoke testing ideas with fast step-projects.
