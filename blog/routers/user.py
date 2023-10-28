from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schema, models
from ..database import get_db
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",

    tags=["user"]
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/", response_model=schema.ShowUser, status_code= status.HTTP_201_CREATED)
def create_user(request:schema.User, db:Session = Depends(get_db)):
    hashed_password =  pwd_context.hash(request.password)
    new_user = models.User(
                           name = request.name, 
                           email = request.email, 
                           password = hashed_password
                           )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[schema.ShowUser])
def show_user(db:Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/user/{id}", response_model=schema.ShowUser)
def user_detail(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with {id} not available!")
    return user 

