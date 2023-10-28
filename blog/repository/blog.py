from fastapi import Response, status, HTTPException
from requests import session
from sqlalchemy.orm import Session
from .. import models, schema

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def blog_detail(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with {id} not available!")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with {id} not available!"}

    return blog 


def create(request:schema.Blog, db:Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog) #to add blog to db 
    db.commit() #execute
    db.refresh(new_blog) # to return newly created blog
    return new_blog


def delete(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return f"Blog {id} deleted successfully"


def update(id:int, request:schema.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found")

    # Update the individual blog object with the request data
    for field, value in request.dict().items():
        setattr(blog, field, value)

    db.commit()  # Make sure you commit the changes

    return {'message': f"Blog {id} updated successfully"}