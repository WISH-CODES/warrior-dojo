from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db
from ..auth import get_current_user
from ..models import User

router = APIRouter(
    prefix="/warriors",
    tags=["Warriors"]
)

# GET all warriors owned by current user
@router.get("/", response_model=List[schemas.WarriorOut])
def get_warriors(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(models.Warrior).filter(models.Warrior.owner_id == current_user.id).all()

# GET specific warrior owned by current user
@router.get("/{warrior_id}", response_model=schemas.WarriorOut)
def get_warrior(
    warrior_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    warrior = db.query(models.Warrior).filter(
        models.Warrior.id == warrior_id,
        models.Warrior.owner_id == current_user.id
    ).first()

    if not warrior:
        raise HTTPException(status_code=404, detail="Warrior not found")

    return warrior

# CREATE warrior tied to current user
@router.post("/", response_model=schemas.WarriorOut)
def create_warrior(
    warrior: schemas.WarriorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_warrior = models.Warrior(
        name=warrior.name,
        skill=warrior.skill,
        owner_id=current_user.id
    )
    db.add(db_warrior)
    db.commit()
    db.refresh(db_warrior)
    return db_warrior

# UPDATE warrior if owned by user
@router.put("/{warrior_id}", response_model=schemas.WarriorOut)
def update_warrior(
    warrior_id: int,
    updated_data: schemas.WarriorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    warrior = db.query(models.Warrior).filter(
        models.Warrior.id == warrior_id,
        models.Warrior.owner_id == current_user.id
    ).first()

    if not warrior:
        raise HTTPException(status_code=404, detail="Warrior not found")

    warrior.name = updated_data.name
    warrior.skill = updated_data.skill
    db.commit()
    db.refresh(warrior)
    return warrior

# DELETE warrior if owned by user
@router.delete("/{warrior_id}")
def delete_warrior(
    warrior_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    warrior = db.query(models.Warrior).filter(
        models.Warrior.id == warrior_id,
        models.Warrior.owner_id == current_user.id
    ).first()

    if not warrior:
        raise HTTPException(status_code=404, detail="Warrior not found")

    db.delete(warrior)
    db.commit()
    return {"msg": "Warrior deleted"}
