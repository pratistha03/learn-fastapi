from typing import List
from pydantic import BaseModel
class Blog(BaseModel):
    title: str
    body: str
    class config():
        orm_mode = True
class User(BaseModel):
    email: str
    name: str
    password: str
    class config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    class config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class config():
        orm_mode = True



class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
