# Verify Payment and Create Order
from datetime import datetime
from app.server.utils.messages import *
from app.server.utils.whatsapp import send_whatsapp_message

from app.server.database.crud import (
    get_single_session_transaction,
    update_user_session,
    delete_single_session,
    create_order,
    get_user_profile
)

async def verify_payment(transaction_reference, transaction_status):
   chat_payment_reference = await get_single_session_transaction(transaction_reference)

   if transaction_status == "PAID":

      # Buy Electricity Unit
      electricity_response = "Successfull"

      # Get User Profile
      user_profile = await get_user_profile(chat_payment_reference['session_id'])

      # Create order detail
      if electricity_response == "Failed":
         electricity_order = {
            "user_profile":user_profile,
            "meter_distribution": chat_payment_reference["meter_distribution"],
            "user_meter_number": chat_payment_reference["user_meter_number"],
            "meter_owner": chat_payment_reference["meter_owner"],
            "meter_address": chat_payment_reference["meter_address"],
            "meter_package": chat_payment_reference["meter_package"],
            "user_amount": chat_payment_reference["user_amount"],
            "payment_confirmation": "PAID",
            "unit_confirmation": "Failed",
            "payment_mode": chat_payment_reference["payment_mode"],
            "transaction_reference": transaction_reference,
            "created_at": datetime.utcnow()
         }
         order = await create_order(electricity_order)
         
         payment_message = order_confirmation(order["_id"])

         send_whatsapp_message(chat_payment_reference["user_phone_number"], payment_message)
         message = order_failed(chat_payment_reference["user_order_id"])
         send_whatsapp_message(chat_payment_reference["user_phone_number"], message)

      elif electricity_response == "Successfull":
         electricity_order = {
            "user_profile":user_profile,
            "meter_distribution": chat_payment_reference["meter_distribution"],
            "user_meter_number": chat_payment_reference["user_meter_number"],
            "meter_owner": chat_payment_reference["meter_owner"],
            "meter_address": chat_payment_reference["meter_address"],
            "meter_package": chat_payment_reference["meter_package"],
            "user_amount": chat_payment_reference["user_amount"],
            "payment_confirmation": "PAID",
            "unit_confirmation": "Successfull",
            "token": None,
            "units": None,
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
     
   return True