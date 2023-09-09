from datetime import datetime
import random
from bson.objectid import ObjectId

from app.server.utils.messages import *
from app.server.utils.whatsapp import send_whatsapp_message

from app.server.models.chatbot_models import (
    UserSchema,
    UserProfileSchema,
    UserSessionSchema,
    OrdersSchema
    )

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
    try:
    #    print("Here")
       # Check if session exists
       get_chat = await get_single_session(phoneid)
       if get_chat['user_phone_number'] == phonenumber:
           chat = get_chat
        #    print(chat)
    except:
        created_at = datetime.utcnow()
        # print("Inside Except!")
        user = await get_user(phoneid)
        # print("After getting user!")
        if user:
            if user["username"] == phoneid:
                user = user
                user_profile = await get_user_profile(phoneid)
        else:
            # print("Creating New user!")
           # Create User
            user_data = {
               "username":phoneid,
               "first_name": profilename,
               "email": "chat@energieasebot.ng",
               "created_at": created_at
           }
            user = await create_user(user_data)
            # print("After Creating user!!")
           # Create User Profile
            user_profile_data = {
               "phone_number": phonenumber,
               "phone_id": phoneid,
               "user": user,
               "created_at": created_at
           }
            user_profile = await create_user_profile(user_profile_data)
            # print("After Creating User Profile")
        
        # Create Chat Session
        # print("Before add_user_session")
        try:
            chat_session_data = UserSessionSchema(
            # _id=str(ObjectId()),
            session_id=phoneid,
            user_phone_number=phonenumber,
            user_name=profilename,
            user_profile=user_profile,
            created_at=str(created_at)
            )

            chat = await add_user_session(chat_session_data)
            # print("After add_user_session")
        except Exception as e:
            print(f"Exception in add_user_session: {str(e)}")

        opening = ['hi', 'Hi', 'Hello', 'Hello', 'Hey', 'hey']
        opening_msg = random.choice(opening).upper()

        if text in opening:
            message = welcome_menu(opening_msg, profilename)
            send_whatsapp_message(phonenumber, message)
    
    quit_inputs = ['q', 'Q', 'Quit', 'quit', 'QUIT']

    # Conversation Logic

    if chat["entry_message"]:
        if chat["user_input_1"]:
            if chat["user_input_2"]:
                if chat["user_meter_number"]:
                    if chat["user_amount"]:
                        if chat["user_confirm"]:
                            if text in quit_inputs:
                                message = quit_chat()
                                await delete_single_session(phoneid)
                                send_whatsapp_message(phonenumber, message)
                            else:
                                message = "We are Already Processing Your Order!!!"
                                send_whatsapp_message(phonenumber, message)
                        else:
                            try:
                                check_type = int(text.replace(' ', ''))
                                if check_type == 1:
                                    update_data = ["user_confirm", text]
                                    data = await update_user_session(update_data, phoneid)
                                    # Generate Payment Details
                                    account_name = ""
                                    account_number = ""
                                    bank_name = ""
                    
                                    message = order_payment(data["user_amount"], account_number, account_name, bank_name)
                                    send_whatsapp_message(phonenumber, message)
                                elif check_type == 2:
                                    message = quit_chat()
                                    await delete_single_session(phoneid)
                                    send_whatsapp_message(phonenumber, message)
                                else:
                                    message = "Oops 😓 Please Enter a Valid Input:"
                                    send_whatsapp_message(phonenumber, message)
                            except:
                                if text in quit_inputs:
                                    message = quit_chat()
                                    send_whatsapp_message(phonenumber, message)
                                    await delete_single_session(phoneid)
                                else:
                                    message = "Oops 😓 Please Enter a Valid Amount:"
                                    send_whatsapp_message(phonenumber, message)
                    else:
                        try:
                            check_type = int(text.replace(' ',''))
                            if check_type >= 1000:
                                update_data = ["user_amount", text]
                                data = await update_user_session(update_data, phoneid)
                                message = order_summary(
                                        data["meter_owner"],
                                        data["user_amount"],
                                        data["user_meter_number"],
                                        data["meter_package"],
                                        data["meter_address"]
                                )
                                send_whatsapp_message(phonenumber, message)
                            else:
                                message = "Oops 😓 Please Enter a Valid Amount:"
                                send_whatsapp_message(phonenumber, message)
                        except:
                            if text in quit_inputs:
                                message = quit_chat()
                                send_whatsapp_message(phonenumber, message)
                                await delete_single_session(phoneid)
                            else:
                                message = "Oops 😓 Please Enter a Valid Amount:"
                                send_whatsapp_message(phonenumber, message)
                else:
                    try:
                        if len(text) == 13:
                            update_data = ["user_meter_number", text]
                            await update_user_session(update_data, phoneid)
                            # Validate Meter Number
                            
                            
                            message = bill_amount()
                            send_whatsapp_message(phonenumber, message)
                        else:
                            message = "Oops 😓 Please Enter a Valid Meter Number:"
                            send_whatsapp_message(phonenumber, message)
                    except:
                        if text in quit_inputs:
                            message = quit_chat()
                            send_whatsapp_message(phonenumber, message)
                            await delete_single_session(phoneid)
                        else:
                            message = "Oops 😓 Please Enter a Valid Meter Number:"
                            send_whatsapp_message(phonenumber, message)
            else:
                try:
                    check_type = int(text.replace(' ', ''))
                    if check_type == 1:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 2:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 3:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 4:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 5:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 6:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 7:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 8:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    elif check_type == 9:
                        update_data = ["user_input_2", text]
                        await update_user_session(update_data, phoneid)
                        message = meter_number()
                        send_whatsapp_message(phonenumber, message)
                    else:
                        message = "Oops 😓 Please Enter a Number:"
                        send_whatsapp_message(phonenumber, message)
                except:
                    if text in quit_inputs:
                        message = quit_chat()
                        send_whatsapp_message(phonenumber, message)
                        await delete_single_session(phoneid)
                    else:
                        message = "Oops 😓 Please Enter a Number:"
                        send_whatsapp_message(phonenumber, message)
        else:
            try:
                check_type = int(text.replace(' ', ''))
                if check_type == 1:
                    update_data = ["user_input_1", text]
                    await update_user_session(update_data, phoneid)
                    message = options_menu()
                    send_whatsapp_message(phonenumber, message)
                elif check_type == 2:
                    update_data = ["user_input_1", text]
                    await update_user_session(update_data, phoneid)
                    message = customer_support()
                    send_whatsapp_message(phonenumber, message)
                else:
                    message = "Oops 😓 Please Enter a Number:"
                    send_whatsapp_message(phonenumber, message)
            except:
                if text in quit_inputs:
                    message = quit_chat()
                    send_whatsapp_message(phonenumber, message)
                    await delete_single_session(phoneid)
                else:
                    message = "Oops 😓 Please Enter a Number:"
                    send_whatsapp_message(phonenumber, message)
    else:
        update_data = ["entry_message", opening_msg]
        await update_user_session(update_data, phoneid)
