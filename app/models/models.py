from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    journal_entries = relationship("JournalEntry", back_populates="user")


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User", back_populates="journal_entries")


class MoodLog(Base):
    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True, index=True)
    mood = Column(String, index=True)
    tags = Column(String)
    journal_entry_id = Column(Integer, ForeignKey("journal_entries.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    user = relationship("User")
    journal_entry = relationship("JournalEntry")


class MoodRating(Base):
    __tablename__ = "mood_ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class ReflectionPrompt(Base):
    __tablename__ = "reflection_prompts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class ReflectionAnswer(Base):
    __tablename__ = "reflection_answers"

    id = Column(Integer, primary_key=True, index=True)
    journal_entry_id = Column(Integer, ForeignKey("journal_entries.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    prompt_id = Column(Integer, ForeignKey("reflection_prompts.id"))
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    journal_entry = relationship("JournalEntry")
    user = relationship("User")
    prompt = relationship("ReflectionPrompt")
