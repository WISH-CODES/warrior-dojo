from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import schemas, models

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=schemas.UserOut)
def read_current_user(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return current_user
