from sqlalchemy.orm import Session
from app.models.models import MoodLog
from app.schemas.schemas import MoodLogCreate


def create_mood_log(db: Session, mood_log: MoodLogCreate, user_id: int):
    db_log = MoodLog(**mood_log.model_dump(), user_id=user_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_mood_logs_by_user(db: Session, user_id: int):
    return db.query(MoodLog).filter(MoodLog.user_id == user_id).all()
