# 🎯 Standard Agile User Story Template

## Story ID: [EPIC-KEY-101] — [Short Descriptive Title]

**Epic Link:** [Link to Parent Epic]  
**Primary Persona:** [Persona Name]  
**Story Points:** [1 / 2 / 3 / 5 / 8 / 13]  
**Priority:** [Must Have / Should Have / Could Have]

---

### User Story Statement:
> **As a** [Primary Persona],  
> **I want to** [specific action / goal],  
> **So that** [clear business value / outcome].

---

### Acceptance Criteria (Gherkin BDD Format):

#### Scenario 1: Successful Happy Path
* **Given** [precondition state],
* **When** [user performs action],
* **Then** [expected result state occurs],
* **And** [secondary state update occurs].

#### Scenario 2: Validation / Edge Case
* **Given** [user enters invalid data],
* **When** [user submits form],
* **Then** [clear inline error message is displayed],
* **And** [submit button remains disabled until fixed].

#### Scenario 3: Error / System Timeout
* **Given** [the server connection fails],
* **When** [action is attempted],
* **Then** [friendly error toast appears with a Retry option].

---

### Technical & Design Notes:
* **UI/UX Link:** [Figma Component / Wireframe Link]
* **API Endpoints:** `POST /api/v1/resource`
* **Data Fields:** Requires `user_id` (string), `action_type` (enum).

---

### Definition of Done (DoD Checklist):
- [ ] Code implemented and peer-reviewed.
- [ ] Unit test coverage >= 80%.
- [ ] Gherkin scenarios verified in QA / Staging.
- [ ] WCAG 2.1 AA accessibility checked (keyboard & screen reader).
- [ ] Documentation updated.
