# Product Requirements Document (PRD)

## 1. Overview

### 1.1 Purpose
The purpose of this document is to outline the requirements for a service that helps users optimize their credit card rewards. This service analyzes a user's credit card statement and the types of credit cards they have in their wallet, then provides recommendations on which charges should be placed on different cards to maximize rewards and benefits.

### 1.2 Background
Credit card users often have multiple cards, each with its own set of rewards and benefits (e.g., cashback on dining, travel points, grocery discounts). However, users may not always use the optimal card for each purchase, leading to missed opportunities for maximizing rewards. This service addresses that problem by analyzing spending patterns and available credit card rewards, then offering actionable insights to help users make smarter spending decisions.

### 1.3 Objectives
- Provide users with clear recommendations on how to distribute their charges across different credit cards for optimal rewards.
- Increase user awareness and understanding of their credit card benefits.
- Help users maximize the rewards (cashback, points, discounts) they earn from their credit card spending.
- Simplify the decision-making process for users managing multiple credit cards.

---

## 2. Stakeholders

### 2.1 Primary Contacts
| Role           | Name           | GitHub User |
|----------------|----------------|----------------------|
| Product Owner  | Wally Khan       | wfkhan97       |
| Engineering Lead | George Tucker       | [Email/Phone]       |

### 2.2 Additional Stakeholders
*List any additional teams or individuals involved (e.g., marketing, customer support, etc.).*

---

## 3. Product Scope

### 3.1 In Scope
The first version of the product (MVP) will include the following capabilities:

1. **User Input**:
   - Users can upload a CSV file containing their transaction history from one or multiple credit cards.
   - Users can specify the American Express credit card products they hold (these may or may not be represented in the transaction CSV).

2. **Merchant Categorization**:
   - The product will categorize each merchant based on the industry type (e.g., dining, travel, groceries) using the transaction data provided in the CSV.

3. **Rewards Optimization**:
   - For each transaction, the product will analyze the user's selected credit card products to determine if a different card would provide greater rewards for that transaction.
   - This analysis will consider the rewards structure of each card (e.g., bonus points for dining, travel credits).

4. **Output**:
   - The product will generate a file (e.g., CSV or downloadable report) that includes:
     - A list of transactions identified as better suited for a different card.
     - The estimated additional rewards points or value the user could gain by using the optimal card for each transaction.
     - A detailed explanation for each recommendation, including:
       - The categorized merchant type.
       - The rationale for why the alternative card is better (e.g., higher reward rate for the category).

5. **Report Accuracy**:
   - Recommendations will be based solely on the information provided in the uploaded transaction CSV and the user-specified credit card products.
   - Only American Express credit cards will be supported in this MVP.

### 3.2 Out of Scope
The following features are not included in this MVP and may be considered for future releases:
- Support for credit cards from other issuers (e.g., Visa, Mastercard, Discover).
- Real-time integration with credit card providers or bank accounts.
- Analysis of non-rewards factors such as credit limits, interest rates, or fees.
- Dynamic updates to credit card reward structures or promotions.
- Advanced visualizations or interactive dashboards for the recommendations.
- Multi-user support or sharing capabilities.
- Recommendations that involve opening new credit cards or applying for additional products.
- Support for input file formats other than CSV.

---

## 4. User Stories & Requirements

### 4.1 User Personas
*Briefly describe the target users, their roles, needs, and goals.*

### 4.2 User Stories
| ID   | User Story                                        | Priority | Notes             |
|------|---------------------------------------------------|----------|-------------------|
| US-01| As a [user], I want to [action], so that [goal]. | High     | [Additional notes]|
| US-02| As a [user], I want to [action], so that [goal]. | Medium   | [Additional notes]|

### 4.3 Functional Requirements
| ID    | Requirement Description                            | User Story ID | Priority | Acceptance Criteria                       |
|-------|----------------------------------------------------|---------------|----------|-------------------------------------------|
| FR-01 | The system shall [requirement description].       | US-01         | High      | [List criteria for acceptance]            |
| FR-02 | The system shall [requirement description].       | US-02         | Medium    | [List criteria for acceptance]            |

---

## 5. UX/UI Requirements

### 5.1 Wireframes / Mockups
*Insert or link to wireframes, mockups, or design prototypes.*

### 5.2 User Flows
*Describe the primary user flows, including main actions and navigation.*

---

## 6. Technical Requirements

### 6.1 Architecture
*Outline the expected architecture or system design.*

### 6.2 Data Requirements
*Describe the data structure, storage, and retrieval needs.*

### 6.3 Security & Compliance
*List any security, privacy, or compliance requirements.*

---

## 7. Non-Functional Requirements

| Category             | Requirement                                             |
|----------------------|---------------------------------------------------------|
| Performance          | Describe any performance requirements (e.g., load times, scalability). |
| Reliability          | Define reliability goals (e.g., uptime, error rates).   |
| Usability            | Outline usability standards or accessibility requirements. |
| Maintainability      | Specify maintenance requirements or technical debt constraints. |
| Documentation        | List required documentation, including user guides and developer documentation. |

---

## 8. Milestones & Timeline

### 8.1 Major Milestones
| Milestone           | Description                   | Target Date | Status |
|---------------------|-------------------------------|-------------|--------|
| Kickoff             | Initial project kickoff       | [Date]      | [Status]|
| MVP Completion      | First version of the product  | [Date]      | [Status]|
| Final Release       | Full product release          | [Date]      | [Status]|

### 8.2 Timeline
*Include a timeline or Gantt chart for a high-level view of the project.*

---

## 9. Risks & Dependencies

### 9.1 Risks
| Risk                 | Description                                     | Mitigation Strategy                      |
|----------------------|-------------------------------------------------|------------------------------------------|
| [Risk name]          | [Description of risk]                           | [How to mitigate]                        |

### 9.2 Dependencies
*List any external dependencies (e.g., third-party tools, teams, etc.).*

---

## 10. Appendix

### 10.1 Glossary
*Define any technical terms or acronyms.*

### 10.2 References
*Link to additional documentation, research, or resources.*
