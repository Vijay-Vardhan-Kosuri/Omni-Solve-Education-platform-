# OmniSolve EduClear - Academic Doubt Clarification Platform

OmniSolve EduClear is a full-stack web application engineered for students to clarify academic doubts across Mathematics, Physics, Chemistry, Computer Science, Biology, and General Aptitude.

---

## Features

- **Step-by-Step Doubt Solvers**: Heuristic analytical engines for Math, Physics, Chemistry, CS, Biology, and Aptitude.
- **Q&A Community Forum**: Post questions, vote on helpful answers, and get verified helper solutions.
- **Interactive Scratchpad Whiteboard**: Draw formulas, diagrams, and math figures with responsive canvas tools.
- **Study Flashcards & Note Editor**: Spaced-repetition study decks and Markdown/LaTeX student note editor.
- **Zero-Dependency Python Backend**: Powered by Django 6.0 REST APIs with automated database migrations and seeding.

---

## Dependencies

- **Python**: Python 3.13 or Python 3.10+
- **Node.js**: Node.js 18+ (optional for npm scripts)
- **Django**: Django 6.0+
- **Docker**: Docker & Docker Compose (optional for container deployment)

---

## Installation

### 1. Clone & Set Up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/omnisolve-educlear.git
cd omnisolve-educlear

# Create and activate Python virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Or install JS dependencies (optional)
npm install
```

---

## Build & Database Setup

```bash
# Apply Django migrations
python manage.py makemigrations
python manage.py migrate

# Seed database with sample doubts, flashcards, and forum threads
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings'); django.setup(); from knowledge_base.seed_data import seed_database; seed_database()"
```

---

## Run Instructions

### Option 1: Direct Python Entry Point (Recommended)

```bash
python main.py
# or
python app.py
```

### Option 2: Django Manage Command

```bash
python manage.py runserver 127.0.0.1:8000
```

### Option 3: Npm Scripts

```bash
npm start
```

### Option 4: Docker Container Deployment

```bash
# Build Docker image
docker build -t educlear-platform:latest .

# Run Docker container
docker run -p 8000:8000 educlear-platform:latest

# Or using docker-compose
docker-compose up --build
```

Access the application in your browser at: **`http://127.0.0.1:8000`**

---

## Running Automated Tests & Coverage

```bash
# Run Django unit tests
python manage.py test

# Run tests with Pytest and coverage
pytest --cov=. tests/
```

---

## Project Structure

```
omnisolve-educlear/
├── manage.py                   # Django CLI entrypoint
├── main.py                     # Main application entry point
├── app.py                      # WSGI/ASGI entry point
├── Makefile                    # Build automation Makefile
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Multi-container Compose spec
├── requirements.txt            # Python dependencies manifest
├── Pipfile & Pipfile.lock      # Pipenv lockfile
├── package.json & lock         # Node.js build manifest
├── doubts/                     # Doubts app (models, views, APIs)
├── forum/                      # Q&A Community forum app
├── flashcards/                 # Flashcards, Notes & Whiteboard app
├── knowledge_base/             # Analytical solver engines (Math, Phys, Chem, CS, Bio, Apt)
├── templates/                  # Single Page Application HTML shell
├── static/                     # Glassmorphic CSS & Vanilla JS modules
└── tests/                      # Automated test suite (Pytest & Django unit tests)
```

---

## License

Proprietary and Confidential. All Rights Reserved.
