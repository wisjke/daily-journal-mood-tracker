from sqlalchemy.orm import Session
from sqlalchemy import func, and_, text
from app.models.models import MoodRating
from app.schemas.schemas import MoodRatingCreate
from datetime import date


def upsert_today_rating(db: Session, user_id: int, data: MoodRatingCreate):
    today = date.today()

    existing = db.query(MoodRating).filter(
        and_(
            MoodRating.user_id == user_id,
            func.DATE(MoodRating.created_at) == today
        )
    ).first()

    if existing:
        existing.score = data.score
        db.commit()
        db.refresh(existing)
        return existing
    else:
        rating = MoodRating(score=data.score, user_id=user_id)
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return rating


def get_average_mood_trend(db: Session, user_id: int, interval: str = "day"):
    format_map = {
        "day": "YYYY-MM-DD",
        "week": "IYYY-IW",
        "month": "YYYY-MM"
    }
    date_format = format_map.get(interval, "YYYY-MM-DD")

    query = """
        SELECT TO_CHAR(created_at, :format) AS period,
               ROUND(AVG(score), 2) AS average_score
        FROM mood_ratings
        WHERE user_id = :user_id
        GROUP BY period
        ORDER BY period
    """

    results = db.execute(text(query), {"format": date_format, "user_id": user_id}).fetchall()
    return [{"period": r[0], "average_score": float(r[1])} for r in results]
