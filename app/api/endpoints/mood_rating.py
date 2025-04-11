from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.auth import get_current_user
from app.models.models import User
from app.schemas.schemas import MoodRatingCreate, MoodRating
from app.crud import mood_rating as crud

router = APIRouter()


@router.post("/", response_model=MoodRating)
def rate_or_update_today(
    data: MoodRatingCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    if not (1 <= data.score <= 10):
        raise HTTPException(status_code=400, detail="Score must be between 1 and 10")
    return crud.upsert_today_rating(db, user.id, data)


@router.get("/trends")
def get_rating_trends(
    interval: str = Query("day", enum=["day", "week", "month"]),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.get_average_mood_trend(db, user.id, interval)
