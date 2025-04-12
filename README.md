# Daily Journal & Mood Tracker

A FastAPI-powered web application for journaling and emotional well-being. Users can write rich-text entries, track moods with tags, reflect using guided questions, and visualize mood trends. The app supports authentication, data export (PDF/Markdown), and is ready for CI/CD with Docker support.

## Table of Contents
- [🚀 Features](#-features)
- [🏗 Project Structure](#️-project-structure)
- [⚙️ Getting Started](#️-getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Configure Environment](#2-configure-environment)
  - [3. Run with Docker](#3-run-with-docker)
- [🧪 Testing & Linting](#-testing--linting)
- [📥 API Endpoints](#-api-endpoints)
  - [🔐 Authentication](#-authentication)
  - [👤 Users](#-users)
  - [📓 Journal Entries](#-journal-entries)
  - [😊 Mood](#-mood)
  - [⭐️ Mood Rating](#-mood-rating)
  - [🧠 Reflection](#-reflection)
- [🔍 Interactive Docs](#-interactive-docs)

## 🚀 Features

- 🔐 User Authentication (JWT)
- 🗒️ Rich-text Journal Entries
- 😊 Mood Logging with Tags
- 📈 Mood Trend Visualization
- 🧠 Reflective Prompts
- 📤 Export Journal to PDF / Markdown
- ✅ Tests, Linting, CI/CD
- 🐳 Docker Support

## 🏗️ Project Structure

```
├── .github/                  
├── app/
│   ├── api/                 # Route handlers
│   ├── core/                # Auth, config, security
│   ├── crud/                # Database logic
│   ├── db/                  # DB session/config
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   ├── tests/               # Test suite
│   └── main.py              # FastAPI entry point
├── .env                     # Environment config
├── .flake8                  # Linter config
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
└── requirements.txt
```

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/wisjke/daily-journal-mood-tracker.git
cd daily-journal-mood-tracker
```

### 2. Configure Environment
Create a `.env` file:
```
DATABASE_URL=postgresql://postgres:password@db:5432/postgres
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Run with Docker
```bash
docker-compose up --build
```

## 🧪 Testing & Linting
```bash
# Run tests
pytest .

# Run linter
flake8 .
```

## 📥 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /token   | Login for access token |

### 👤 Users
| Method | Endpoint  | Description |
|--------|-----------|-------------|
| POST   | /users/   | Register user |
| GET    | /users/me | Get current user profile |

### 📓 Journal Entries
| Method | Endpoint                       | Description |
|--------|--------------------------------|-------------|
| POST   | /journal/                      | Create journal entry |
| GET    | /journal/                      | List journal entries |
| GET    | /journal/{entry_id}            | Read single journal entry |
| PUT    | /journal/{entry_id}            | Update journal entry |
| DELETE | /journal/{entry_id}            | Delete journal entry |
| GET    | /journal/{entry_id}/export/pdf | Export as PDF |
| GET    | /journal/{entry_id}/export/markdown | Export as Markdown |

### 😊 Mood
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /mood/   | Log mood |
| GET    | /mood/   | Get mood logs |

### ⭐ Mood Rating
| Method | Endpoint            | Description |
|--------|---------------------|-------------|
| POST   | /mood-rating/       | Rate or update today |
| GET    | /mood-rating/trends | View rating trends |

### 🧠 Reflection
| Method | Endpoint                   | Description |
|--------|----------------------------|-------------|
| GET    | /reflection/prompt/daily   | Get daily prompt |
| POST   | /reflection/prompt/answer  | Answer reflection prompt |

## 🔍 Interactive Docs
Once running, explore the interactive API documentation:
- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc
