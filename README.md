# Health Claims API

A minimal backend service simulating a **health insurance claim workflow**.  
Provides REST API endpoints to **submit new claims** and **retrieve claim status**, with simple validation for:

- Member eligibility  
- Benefit limits  
- Fraud detection (claim amount vs procedure average cost)

---

## Architecture Decisions

[Data Modelind and Architecture document](https://docs.google.com/document/d/1w0t9b9oB1Mthh3tCRCFE47bGrfieID2M6FVxRnbYfQs/edit?usp=sharing)

- **Framework:** Django + Django REST Framework (DRF)  
- **Database:** SQLite 
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


## Getting Started

### 1. Clone the repository


git clone https://github.com/Muyizereberissa/Health_Claim.git
### 2. Create and activate a virtual environment

### Windows PowerShell
python -m venv venv
.\venv\Scripts\activate

### macOS/Linux
python -m venv venv
source venv/bin/activate

### Install dependencies

 pip install -r requirements.txt

### Apply migrations
 python manage.py migrate

### Run server

python manage.py runserver

### Improvements for production

- Change database from SQLite to PostgreSQL 
- Use environment variables for secrets, configure HTTPS
- Add caching, async tasks for claim validation if heavy
- Deployment: Docker,  CI/CD pipeline
- Add integration tests, API tests


API: http://127.0.0.1:8000/api/claims/

Admin: http://127.0.0.1:8000/admin/

