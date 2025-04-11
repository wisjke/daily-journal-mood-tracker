from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import models
from app.db.database import engine
from app.api.endpoints import mood, users, journal, auth, reflection, mood_rating

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Journal & Mood Tracker",
    description="API for tracking journal entries",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(journal.router, prefix="/journal", tags=["Journal Entries"])
app.include_router(mood.router, prefix="/mood", tags=["Mood"])
app.include_router(mood_rating.router, prefix="/mood-rating", tags=["Mood Rating"])
app.include_router(reflection.router, prefix="/reflection", tags=["Reflection"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Journal & Mood Tracker API"}
