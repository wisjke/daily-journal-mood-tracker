from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class JournalEntryBase(BaseModel):
    title: str
    content: str


class JournalEntryCreate(JournalEntryBase):
    pass


class JournalEntry(JournalEntryBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class MoodLogBase(BaseModel):
    mood: str
    tags: Optional[str] = None


class MoodLogCreate(MoodLogBase):
    journal_entry_id: int


class MoodLog(MoodLogBase):
    id: int
    user_id: int
    journal_entry_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MoodRatingCreate(BaseModel):
    score: int


class MoodRating(BaseModel):
    id: int
    user_id: int
    score: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReflectionPrompt(BaseModel):
    id: int
    text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReflectionAnswerCreate(BaseModel):
    journal_entry_id: int
    prompt_id: int
    answer: str


class ReflectionAnswer(BaseModel):
    id: int
    journal_entry_id: int
    prompt_id: int
    answer: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
