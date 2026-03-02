## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd health_claims
2. Create and activate a virtual environment
# Windows PowerShell
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply database migrations
python manage.py migrate

5. Create a superuser
python manage.py createsuperuser

6. Run the development server
python manage.py runserver

API: http://127.0.0.1:8000/api/claims/

Admin: http://127.0.0.1:8000/admin/