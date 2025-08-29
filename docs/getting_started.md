# Getting Started with Cognate

## Backend (FastAPI)
- Python 3.10+
- Install dependencies: `pip install -r backend-fastapi/requirements.txt`
- Run: `uvicorn backend-fastapi.main:app --reload`

## Backend (Flask)
- Python 3.10+
- Install dependencies: `pip install -r backend-flask/requirements.txt`
- Run: `flask --app backend-flask/main run`

## Frontend (Next.js)
- Node.js 18+
- Install: `npm install` in `web-nextjs/`
- Run: `npm run dev`

## Desktop (PyQt6)
- Python 3.10+
- Install: `pip install PyQt6`
- Run: `python desktop/App.py`

## Mobile (React Native)
- Node.js 18+, Expo CLI
- Install: `npm install` in `mobile-react-native/`
- Run: `expo start`

## Mobile (Kotlin)
- Android Studio
- Open `mobile-kotlin` as a project.

## Database
- PostgreSQL
- See `database/schema.sql` for the initial schema.

## DevOps
- Docker: `docker build -t cognate .`
- Azure DevOps: See `devops/azure-pipelines.yml`
