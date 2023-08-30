from fastapi import FastAPI, APIRouter, Query, status, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.server.utils.whatsapp import send_whatsapp_message
from app.server.utils.messages import welcome_menu

from app.server.database.crud import add_user_session, update_user_session, get_single_session

import random
from datetime import datetime
from cachetools import LRUCache

router = APIRouter()

# Initialize a cache to store processed message IDs
# processed_message_ids = LRUCache(maxsize=20)  # Adjust maxsize as needed

@router.get("/")
async def buy_electricity_webhook_verification(hub_mode: str = Query(..., alias='hub.mode'), verify_token: str = Query(..., alias='hub.verify_token'), challenge: int = Query(..., alias='hub.challenge')):
   
   VERIFY_TOKEN = "buyelectricitybot"

   if hub_mode == 'subscribe' and verify_token == VERIFY_TOKEN:
      #return {'hub.challenge': challenge}
      return JSONResponse(content=challenge, status_code=status.HTTP_200_OK)
   else:
      raise HTTPException(detail="Forbidden", status_code=status.HTTP_403_FORBIDDEN)

@router.post("/", status_code=status.HTTP_200_OK)
async def buy_electricity_webhook(request: Request):
   response = await request.json()
   # print(response)
   if ('object' in response) and ('entry' in response):
      if response['object'] == 'whatsapp_business_account':
         try:
            for entry in response['entry']:
               phone_number = entry['changes'][0]['value']['metadata']['display_phone_number']
               phone_id = entry['changes'][0]['value']['metadata']['phone_number_id']
               profile_name = entry['changes'][0]['value']['contacts'][0]['profile']['name']
               whatsapp_id = entry['changes'][0]['value']['contacts'][0]['wa_id']
               from_id = entry['changes'][0]['value']['messages'][0]['from']
               message_id = entry['changes'][0]['value']['messages'][0]['id']
               timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
               text = entry['changes'][0]['value']['messages'][0]['text']['body']

               # if message_id in processed_message_ids:
               #      continue  # Skip processing duplicate message
               
               # processed_message_ids[message_id] = True

               opening_inputs = ['hi', 'Hi', 'hello', 'Hello', 'Hey', 'hey']
               quit_inputs = ['q', 'Q', 'Quit', 'quit', 'QUIT']
               opening_msg = random.choice(opening_inputs).upper()

               if text in opening_inputs:
                  bot_message = welcome_menu(profile_name, opening_msg)
                  send_whatsapp_message(from_id, bot_message)
                  schema = {
                     "user_phone_number": from_id,
                     "user_name": profile_name,
                     "message_id": message_id,
                     "created_at": datetime.utcnow()
                  }
                  new_user_session = await add_user_session(schema)

               if text:
                  user_session = await get_single_session(message_id)
                  print(user_session['message_id'])
                  print("hello")

                  if "1" in text:
                     send_whatsapp_message(from_id, "user_session['message_id']")
         except:
            pass
         # except Exception as e:
         #    raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)