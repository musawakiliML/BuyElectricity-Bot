from fastapi import FastAPI, APIRouter, Query, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.server.utils.whatsapp import send_whatsapp_message

router = APIRouter()

@router.get("/")
async def buy_electricity_webhook(hub_mode: str = Query(..., alias='hub.mode'), verify_token: str = Query(..., alias='hub.verify_token'), challenge: int = Query(..., alias='hub.challenge')):
   
   VERIFY_TOKEN = "buyelectricitybot"

   if hub_mode == 'subscribe' and verify_token == VERIFY_TOKEN:
      #return {'hub.challenge': challenge}
      return JSONResponse(content=challenge, status_code=status.HTTP_200_OK)
   else:
      raise HTTPException(detail="Forbidden", status_code=status.HTTP_403_FORBIDDEN)