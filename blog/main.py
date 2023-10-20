from turtle import title
from fastapi import Depends, FastAPI

from blog import models, schema
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create_blog(request:schema.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog) #to add blog to db 
    db.commit() #execute
    db.refresh(new_blog) # to reruen newly created blog
    return new_blog