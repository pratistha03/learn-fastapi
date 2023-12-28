from lib2to3.pytree import Base
from pydantic import BaseModel


class SignupSchema(BaseModel):
    display_name: str
    email: str
    password: str

   

class LoginSchema(BaseModel):
    email: str
    password: str

class UserSchema(BaseModel):
    uid: str
    display_name: str
    email: str
    password: str

class UserTokenSchema(BaseModel):
    user_id: int
    token: str
