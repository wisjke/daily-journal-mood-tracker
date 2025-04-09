from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.db.database import get_db
from app.models.models import User
from app.schemas.schemas import JournalEntryCreate, JournalEntry as JournalEntrySchema
from app.crud import journal as crud_journal

router = APIRouter()


@router.post("/", response_model=JournalEntrySchema, status_code=status.HTTP_201_CREATED)
def create_journal_entry(
    entry: JournalEntryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_journal.create_journal_entry(db, entry, current_user.id)


@router.get("/", response_model=List[JournalEntrySchema])
def read_journal_entries(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_journal.get_journal_entries(db, current_user.id, skip, limit)


@router.get("/{entry_id}", response_model=JournalEntrySchema)
def read_journal_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    entry = crud_journal.get_journal_entry(db, entry_id, current_user.id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return entry


@router.put("/{entry_id}", response_model=JournalEntrySchema)
def update_journal_entry(
    entry_id: int,
    entry: JournalEntryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_entry = crud_journal.get_journal_entry(db, entry_id, current_user.id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return crud_journal.update_journal_entry(db, db_entry, entry)


@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_journal_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_entry = crud_journal.get_journal_entry(db, entry_id, current_user.id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    crud_journal.delete_journal_entry(db, db_entry)
    return None
