from sys import displayhook
from typing import List
from MySQLdb import IntegrityError
import pyrebase
import json
from fastapi import APIRouter, HTTPException, Depends, Header, status
from fastapi.responses import JSONResponse
from firebase_admin import auth
from sqlalchemy.orm import Session
from database import get_db
from models import User

from schema import LoginSchema, SignupSchema, UserSchema, UserTokenSchema



router = APIRouter()

pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))



@router.post("/login")
async def login(user_data: LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
       user = pb.auth().sign_in_with_email_and_password(email, password)
       jwt = user['idToken']
       print(jwt)
       return JSONResponse(content={'token': jwt}, status_code=200)
    
    except:
       return HTTPException(detail={'message': 'Invalid Credentials'}, status_code=400)

   


@router.post("/signup")
async def create_account(user_data: SignupSchema, db:Session = Depends(get_db)):
    email = user_data.email
    password = user_data.password
    display_name = user_data.display_name
    if email is None or password is None:
       return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
   
    try:
        user = auth.create_user(email = email, password = password, display_name = display_name)
        save_user_locally = User(id = user.uid, email = user.email, password = password, display_name = user.display_name)
        db.add(save_user_locally)
        db.commit()
        db.refresh(save_user_locally)
        return JSONResponse(
            content={"message":f"User created successfully {user.uid}"},
            status_code=status.HTTP_202_ACCEPTED
        )
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Account with provided email '{email}' already exists"
        )

async def validate_token(token:str = Header()):
    #  Check if the token is provided and not empty
    if not token:
        raise HTTPException(status_code=401, detail="Token not provided")

    try:
        # Verify the ID token
        user = auth.verify_id_token(token)
        return {"uid": user["uid"]}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")


@router.get("/secure-endpoint")
async def secure_endpoint(current_user: dict = Depends(validate_token)):
    return {"message": "This is a secure endpoint", "user": current_user}



# @router.get("/user", response_model=List[UserSchema])
# def get_user(db:Session = Depends(get_db)):
#     users = db.query(User).all()
#     return users

@router.get('/user')
def get_user():
    try:
        # List all users
        user_list = auth.list_users() 
        users=[]
        for user in user_list.users:
            user_info = {
            "uid": user.uid,
            "display_name": user.display_name,
            "email": user.email
            }
            users.append(user_info)

        # users = [user.uid for user in user_list.users]
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    

@router.post("/fcm/save")
def save_device_token(request: UserTokenSchema, token: str, user: int, db:Session = Depends(get_db)):
    user_token = User(**request.dict())
    db.add(user_token)
    db.commit()
    db.refresh(user_token)
    return user_token