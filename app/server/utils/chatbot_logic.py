from datetime import datetime
import random

from app.server.utils.messages import *
from app.server.utils.whatsapp import send_whatsapp_message

from app.server.database.crud import (
    get_single_session,
    update_user_session,
    add_user_session,
    delete_single_session,
    get_user,
    create_user,
    create_order,
    create_user_profile,
    get_user_profile
)

async def handle_whatsapp_chat(phonenumber, text, profilename, phoneid):
    # print(text)
   # Check if session exists
    try:
       get_chat = await get_single_session(phoneid)
       if get_chat['phone_number'] == phonenumber:
           chat = get_chat
    except:
        # print("here")
        user = await get_user(phoneid)
        # print("after")
        if user:
            if user["username"] == phoneid:
                user = user
                user_profile = await get_user_profile(phoneid)
        else:
        # print("next")
           # Create User
           created_at = datetime.utcnow()
           user_data = {
               "username":phoneid,
               "first_name": profilename,
               "email": "chat@energieasebot.ng",
               "created_at": created_at
           }
           user = await create_user(user_data)

           # Create User Profile
           user_profile_data = {
               "phone_number": phonenumber,
               "phone_id": phoneid,
               "user": user,
               "created_at": created_at
           }
           user_profile = await create_user_profile(user_profile_data)

        # Create Chat Session
        chat_session_data = {
            "session_id": phoneid,
            "user_phone_number": phonenumber,
            "user_name": profilename,
            "user_profile": user_profile
        }
        chat = await add_user_session(chat_session_data)

        opening = ['hi', 'Hi', 'Hello', 'Hello', 'Hey', 'hey']
        opening_msg = random.choice(opening).upper()

        if text in opening:
            message = welcome_menu(opening_msg, profilename)
            send_whatsapp_message(phonenumber, message)
    
    # quit_inputs = ['q', 'Q', 'Quit', 'quit', 'QUIT']

    # # Conversation Logic

    # if chat["entry_message"]:
    #     pass
    # else:
    #     update_data = ["entry_message", opening_msg]
    #     data = await update_user_session(update_data, phoneid)
