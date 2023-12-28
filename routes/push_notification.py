# import os
from fastapi import APIRouter, HTTPException
# from fastapi.responses import JSONResponse
from firebase_admin import messaging


router = APIRouter()


    # Broadcast a push notification to all devices.
# @router.post('/broadcast_notification')
# async def broadcast_notification(title: str, body: str):
#        # Fetch all device tokens from your database or any other source
#     device_tokens = ["DEVICE_TOKEN_1", "DEVICE_TOKEN_2", "..."]

#     async with httpx.AsyncClient() as client:
#         tasks = [
#             send_push_notification(token, title, body)
#             for token in device_tokens
#         ]
#         responses = await asyncio.gather(*tasks)

#     return JSONResponse(content={"message": "Broadcast successful", "responses": responses})




@router.post("/send_notification")
async def send_notification(device_token: str, title: str, message: str):
    url = "https://fcm.googleapis.com/fcm/send"
    message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=message,
            ),
            token="cmY1Cz2GsOQ6NiIuk2K6DI:APA91bHJ-Ey3Kr84xUDAY_sYB2HdGhlT3P4Al9tchdx7AyGQZ6CyLsY4z_pqAMzfaNcAOkPL2kTlNAcnbz6X0_iRXfOzYOk0O-3B5Hua-vB_Ma1kWVhqeLZT0tCFlXFPEVZp7I-wBMJs",
        )
    response = messaging.send(message)
    return {"success": True, "result": response}
   