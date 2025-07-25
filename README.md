# 🚀 Secure FastAPI Application

A secure RESTful API built with **FastAPI**, featuring **JWT-based authentication**, **Pydantic validation**, and **Docker support**.

## 📁 Project Structure


---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/secure-fastapi-app.git
cd secure-fastapi-app

2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

If you get a multipart error, run:
pip install python-multipart

🚀 Run the Application Locally

uvicorn app.main:app --reload

Visit the interactive Swagger docs:
http://127.0.0.1:8000/docs

🔐 Authentication Endpoints
Method	Endpoint	Description
POST	/auth/token	Login and get JWT token
GET	/auth/me	Get current user (requires token)

✅ Sample Login Payload
{
  "username": "testuser",
  "password": "testpassword"
}

Use the token received to authorize /auth/me.

🧪 Run Tests
If tests are included, run:
pytest

🐳 Docker Instructions
1. Build Docker Image

docker build -t secure-fastapi-app .

2. Run Container
docker run -d -p 8000:8000 secure-fastapi-app

⚙️ GitHub Actions CI/CD
This project includes a CI workflow using GitHub Actions:

Lint code

Run tests

Optionally deploy to Docker Hub / cloud

Workflow file: .github/workflows/ci.yml

☁️ Deployment Options
You can deploy to:

Render: render.com

Railway: railway.app

Fly.io: fly.io

Add your environment variables like SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, etc.

🧠 Technologies Used
FastAPI

Pydantic

JWT

Uvicorn

Docker

GitHub Actions

yaml

---

