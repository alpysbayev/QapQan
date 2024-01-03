import schemas as sch
import models as mdl
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import converters as cnv

def create_user(user: sch.UserCreate, db: Session):
    db_user: mdl.User = cnv.UserConverter.to_model(user=user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

