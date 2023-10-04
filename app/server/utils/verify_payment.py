# Verify Payment and Create Order
from datetime import datetime
from app.server.utils.messages import *
from app.server.utils.whatsapp import send_whatsapp_message
from app.server.utils.vtpass_functions import vtpass, credentials, generated_request_id

from app.server.database.crud import (
    get_single_session_transaction,
    update_user_session,
    delete_single_session,
    create_order,
    get_user_profile
)

async def verify_payment(transaction_reference, transaction_status):
   try:
      chat_payment_reference = await get_single_session_transaction(transaction_reference)

      if transaction_status == "PAID":

         # Buy Electricity Unit
         request_id = generated_request_id()
         if chat_payment_reference["meter_distribution"] == "IKEDC":
            billers_id = "ikeja-electric"
         elif chat_payment_reference["meter_distribution"] == "AEDC":
            billers_id = "abuja-electric"
         elif chat_payment_reference["meter_distribution"] == "EEDC":
            billers_id = "enugu-electric"
         elif chat_payment_reference["meter_distribution"] == "EKEDC":
            billers_id = "eko-electric"
         elif chat_payment_reference["meter_distribution"] == "IBEDCO":
            billers_id = "ibadan-electric"
         elif chat_payment_reference["meter_distribution"] == "JED":
            billers_id = "jos-electric"
         elif chat_payment_reference["meter_distribution"] == "KAEDCO":
            billers_id = "kano-electric"
         elif chat_payment_reference["meter_distribution"] == "KEDCO":
            billers_id = "kaduna-electric"
         elif chat_payment_reference["meter_distribution"] == "PHED":
            billers_id = "portharcourt-electric"
         elif chat_payment_reference["meter_distribution"] == "BEDC":
            billers_id = "benin-electric"

         electricity_response = vtpass.purchase_electricity_unit(
            request_id,
            billers_id,
            # chat_payment_reference["user_meter_number"],
            "1111111111111",
            chat_payment_reference["meter_type"],
            int(chat_payment_reference["user_amount"]),
            chat_payment_reference["user_profile"]["phone_number"],
            credentials
         )
         # Get User Profile
         user_profile = await get_user_profile(chat_payment_reference['session_id'])

         # Create order detail
         try:
            if electricity_response["code"] == "000":
               if electricity_response["content"]["transactions"]["status"] == "delivered":
                  tokens = str(electricity_response["token"].split(':')[1])
                  units = electricity_response["units"]
                  electricity_order = {
                     "user_profile":user_profile,
                     "meter_distribution": chat_payment_reference["meter_distribution"],
                     "user_meter_number": chat_payment_reference["user_meter_number"],
                     "meter_owner": chat_payment_reference["meter_owner"],
                     "meter_address": chat_payment_reference["meter_address"],
                     "meter_type": chat_payment_reference["meter_type"],
                     "user_amount": chat_payment_reference["user_amount"],
                     "payment_confirmation": "PAID",
                     "unit_confirmation": "Successfull",
                     "token": tokens,
                     "units": units,
                     "payment_mode": chat_payment_reference["payment_mode"],
                     "transaction_reference": transaction_reference,
                     "created_at": str(datetime.utcnow())
                  }
                  order = await create_order(electricity_order)

                  payment_message = order_confirmation(order["_id"])

                  send_whatsapp_message(chat_payment_reference["user_phone_number"], payment_message)

                  message = order_successful(
                     order['units'],
                     order['_id'],
                     order['user_meter_number'],
                     order['token']
                  )
                  send_whatsapp_message(chat_payment_reference['user_phone_number'], message)
                  message = quit_chat()
                  send_whatsapp_message(chat_payment_reference['user_phone_number'], message)

                  await delete_single_session(chat_payment_reference["session_id"])

            else:
               response = electricity_response["code"]
               electricity_order = {
                     "user_profile":user_profile,
                     "meter_distribution": chat_payment_reference["meter_distribution"],
                     "user_meter_number": chat_payment_reference["user_meter_number"],
                     "meter_owner": chat_payment_reference["meter_owner"],
                     "meter_address": chat_payment_reference["meter_address"],
                     "meter_type": chat_payment_reference["meter_type"],
                     "user_amount": chat_payment_reference["user_amount"],
                     "payment_confirmation": "PAID",
                     "unit_confirmation": response,
                     "payment_mode": chat_payment_reference["payment_mode"],
                     "transaction_reference": transaction_reference,
                     "created_at": datetime.utcnow()
                  }
               
               order = await create_order(electricity_order)
               
               payment_message = order_confirmation(order["_id"])

               send_whatsapp_message(chat_payment_reference["user_phone_number"], payment_message)
               message = order_failed(chat_payment_reference["_id"])
               send_whatsapp_message(chat_payment_reference["user_phone_number"], message)
         except Exception as e:
            raise {"message": str(e)}
         return True
   except Exception as e:
      raise {"message": str(e)}