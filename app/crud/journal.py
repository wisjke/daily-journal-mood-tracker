from sqlalchemy.orm import Session
from typing import Optional
from app.models.models import JournalEntry
from app.schemas.schemas import JournalEntryCreate


def create_journal_entry(db: Session, entry: JournalEntryCreate, user_id: int) -> JournalEntry:
    db_entry = JournalEntry(
        title=entry.title,
        content=entry.content,
        user_id=user_id
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def get_journal_entries(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(JournalEntry).filter(
        JournalEntry.user_id == user_id
    ).order_by(JournalEntry.created_at.desc()).offset(skip).limit(limit).all()


def get_journal_entry(db: Session, entry_id: int, user_id: int) -> Optional[JournalEntry]:
    return db.query(JournalEntry).filter(
        JournalEntry.id == entry_id,
        JournalEntry.user_id == user_id
    ).first()


def update_journal_entry(db: Session, db_entry: JournalEntry, new_data: JournalEntryCreate):
    db_entry.title = new_data.title
    db_entry.content = new_data.content
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_journal_entry(db: Session, db_entry: JournalEntry) -> None:
    db.delete(db_entry)
    db.commit()
