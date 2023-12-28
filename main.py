from fastapi.middleware import Middleware
import firebase_admin
import os
from firebase_admin import credentials, auth
from fastapi import FastAPI, Request, Header
import pyrebase 
import json
from fastapi.middleware.cors import CORSMiddleware
from routes import authentication, push_notification
from fastapi.security import APIKeyHeader



# firebase_admin app will verify the ID token for the user 
# pyrebase app is the one that lets you sign in with your email and password.


app=FastAPI(
    # docs_url='/'
)
 
# to make sure this is running in case we donot have any apps or firebase admin has initialized any apps 
# Initialize the Firebase Admin SDK

# if not firebase_admin._apps:
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app.include_router(authentication.router, prefix='/auth', tags=['User Authentication using FCM'])
app.include_router(push_notification.router, prefix='/fcm', tags=['Push notification'])


# allow_all = ['*']
# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=allow_all,
#    allow_credentials=True,
#    allow_methods=allow_all,
#    allow_headers=allow_all
# )



# from fastapi import FastAPI, Form
# from onesignal_sdk.client import Client
# # from onesignal_sdk.notification import Notification

# app = FastAPI()

# # Replace these with your OneSignal API key and App ID
# ONESIGNAL_API_KEY = 'your_onesignal_api_key'
# ONESIGNAL_APP_ID = 'your_onesignal_app_id'

# # Define the push notification endpoint
# @app.post("/send_push_notification/")
# async def send_push_notification(device_token: str = Form(...), title: str = Form(...), message: str = Form(...)):
#     client = Client(app_id=ONESIGNAL_APP_ID, rest_api_key=ONESIGNAL_API_KEY)
#     new_notification = Notification(contents={"en": message}, headings={"en": title}, include_player_ids=[device_token])
#     client.send_notification(new_notification)
#     return {"message": "Push notification sent successfully"}



# # to get the device token
# def get_device_token(api_key: str = Depends(APIKeyHeader(name="X-Token"))):
#     if api_key != "valid_device_token":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid device token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return api_key

# @app.get("/secure-endpoint-device-token")
# async def secure_endpoint(device_token: str = Depends(get_device_token)):
#     return {"message": "This is a secure endpoint", "device_token": device_token}

# def on_startup():
#     try:
#         device_token = get_device_token()
#         print(f"Device token retrieved on startup: {device_token}")
#     except HTTPException as e:
#         print(f"Failed to retrieve device token on startup: {e.detail}")

# app.add_event_handler("startup", on_startup)

