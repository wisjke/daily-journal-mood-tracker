from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.schemas import MoodLogCreate, MoodLog
from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.models import User
from app.crud import mood as crud_mood
from typing import List

router = APIRouter()


@router.post("/", response_model=MoodLog, status_code=status.HTTP_201_CREATED)
def log_mood(
    mood_log: MoodLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_mood.create_mood_log(db, mood_log, current_user.id)


@router.get("/", response_model=List[MoodLog])
def get_moods(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_mood.get_mood_logs_by_user(db, current_user.id)
