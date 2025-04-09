from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.db.database import get_db
from app.schemas.schemas import UserCreate, User as UserSchema
from app.crud import users as crud_user

router = APIRouter()


@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    if crud_user.get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
        )
    return crud_user.create_user(db, user)


@router.get("/me", response_model=UserSchema)
def get_current_user_profile(current_user: UserSchema = Depends(get_current_user)):
    return current_user
