# Health Claims API

A minimal backend service simulating a **health insurance claim workflow**.  
Provides REST API endpoints to **submit new claims** and **retrieve claim status**, with simple validation for:

- Member eligibility  
- Benefit limits  
- Fraud detection (claim amount vs procedure average cost)

---

## Architecture Decisions

- **Framework:** Django + Django REST Framework (DRF)  
- **Database:** SQLite (for simplicity; can switch to PostgreSQL for production)  
- **Models:**  

| Model     | Purpose                                      |
|-----------|---------------------------------------------|
| Member    | Represents insured members                   |
| Provider  | Represents hospitals/providers               |
| Procedure | Represents medical procedures               |
| Diagnosis | Represents diagnoses                        |
| Claim     | Stores claims with status, approved amount, and fraud flag |

- **Business IDs:** API accepts `member_id`, `provider_id`, `procedure_code`, and `diagnosis_code` s.  
- **Service Layer:** `ClaimService` handles validation logic.  
- **Serializers:**  
  - `ClaimCreateSerializer` – input for POST requests  
  - `ClaimResponseSerializer` – structured output for GET requests  
- **Unit Tests:** Tests cover claim creation, fraud detection, and inactive member rejection.

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd health_claims
```bash

### 2. Create and activate a virtual environment

```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

### Install dependencies
```bash
 pip install -r requirements.txt
 ```bash

### Apply migrations
```bash
 python manage.py migrate
 ```bash

### Run server
```bash
python manage.py runserver
```bash

API: http://127.0.0.1:8000/api/claims/

Admin: http://127.0.0.1:8000/admin/

