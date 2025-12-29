from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas, oauth2, database

router = APIRouter(
    prefix="/notes",
    tags=['Notes']
)

@router.get("/", response_model=List[schemas.Note])
def get_notes(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    notes = db.query(models.Note).filter(
        models.Note.title.contains(search),
        models.Note.owner_id == current_user.id
    ).limit(limit).offset(skip).all()
    
    return notes

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Note)
def create_notes(note: schemas.NoteCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    new_note = models.Note(owner_id=current_user.id, **note.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

@router.get("/{id}", response_model=schemas.Note)
def get_note(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    note = db.query(models.Note).filter(models.Note.id == id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")

    if note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    return note

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    note_query = db.query(models.Note).filter(models.Note.id == id)
    note = note_query.first()

    if note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} does not exist")

    if note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    note_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Note)
def update_note(id: int, updated_note: schemas.NoteCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    note_query = db.query(models.Note).filter(models.Note.id == id)
    note = note_query.first()

    if note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} does not exist")

    if note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    note_query.update(updated_note.dict(), synchronize_session=False)
    db.commit()

    return note_query.first()
