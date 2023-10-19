from re import template
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from pymango import MongoClient

# from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# conn = MongoClient("mongodb://localhost:27017")

@app.get("/", response_class=HTMLResponse)
def get_notes(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/items/{item_id}")
def read_item(item_id: int, q:str | None = None):
    return {"item_id": item_id, "q": q}