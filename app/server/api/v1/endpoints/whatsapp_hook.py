from fastapi import FastAPI, APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.server.utils.whatsapp import send_whatsapp_message

router = APIRouter()

@router.get("/")
async def buy_electricity_webhook(request: Request):
   
   VERIFY_TOKEN = "buyelectricitybot"
   response = await request.json()
   print(response)
   mode = request.get('hub.mode')
   token = request.get('hub.verify_token')
   challenge = request.get('hub.challenge')

   if mode == 'subscribe' and token == VERIFY_TOKEN:
      print(challenge)
      return JSONResponse(content=challenge, status_code=status.HTTP_200_OK)
   else:
      return JSONResponse(jsonable_encoder("Forbidden"), status_code=status.HTTP_403_FORBIDDEN)