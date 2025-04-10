from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.schemas import ReflectionPrompt, ReflectionAnswer, ReflectionAnswerCreate
from app.core.auth import get_current_user
from app.models.models import User
from app.crud import reflection as crud_reflection

router = APIRouter()


@router.get("/prompt/daily", response_model=ReflectionPrompt)
def get_daily_prompt(db: Session = Depends(get_db)):
    prompt = crud_reflection.get_random_prompt(db)
    if not prompt:
        raise HTTPException(status_code=404, detail="No prompts found")
    return prompt


@router.post("/prompt/answer", response_model=ReflectionAnswer)
def answer_prompt(
    data: ReflectionAnswerCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud_reflection.create_reflection_answer(db, user_id=user.id, data=data)
