from re import template
from typing import Optional, Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


# from .models import Blog
# from pymango import MongoClient

# from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# conn = MongoCli ent("mongodb://localhost:27017")

# @app.get("/", response_class=HTMLResponse)
# def get_notes(request:Request):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.get("/blog" )
def blog(limit=10, published:bool=False):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}

@app.get("/blog/published")
def published():
    return {'data': 'all published blogs'}

@app.get("/blog/{blog_id}")
def blog_detail(blog_id:int):
    return {'data': blog_id}\
    
@app.get("/blog/{id}/comments")
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel): 
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    # return blog
    return {'message': f"blog created with {blog.title}"}