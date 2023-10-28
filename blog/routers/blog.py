import re
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Response

from blog.oauth2 import get_current_user
from blog import schema, models
from blog.database import get_db
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get("/", response_model=List[schema.ShowBlog])
def get_blog(db:Session =Depends(get_db), current_user: schema.User=Depends(get_current_user)):#getting db instance
    return blog.get_all(db)


@router.get("/{id}", response_model=schema.ShowBlog)
def blog_detail(id, response:Response, db:Session = Depends(get_db), current_user: schema.User=Depends(get_current_user)):
    return blog.blog_detail(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request:schema.Blog, db:Session = Depends(get_db), current_user: schema.User=Depends(get_current_user)): #default value depends in the db
    
    return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session = Depends(get_db), current_user: schema.User=Depends(get_current_user)):
    return blog.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schema.ShowBlog)
def update_blog(id, request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User=Depends(get_current_user)):
    return blog.update(id, request, db)




