import schemas
import crud
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db

router = APIRouter()

@router.get("/")
def index():
    return {"message": "Hello World"}


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    crud.create_user(user=user, db=db)
    return {"message": "User created"}
