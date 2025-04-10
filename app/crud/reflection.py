from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.models.models import ReflectionPrompt, ReflectionAnswer
from app.schemas.schemas import ReflectionAnswerCreate


def get_random_prompt(db: Session) -> ReflectionPrompt:
    return db.query(ReflectionPrompt).order_by(func.random()).first()


def create_reflection_answer(db: Session, user_id: int, data: ReflectionAnswerCreate):
    answer = ReflectionAnswer(
        journal_entry_id=data.journal_entry_id,
        prompt_id=data.prompt_id,
        answer=data.answer,
        user_id=user_id,
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer
