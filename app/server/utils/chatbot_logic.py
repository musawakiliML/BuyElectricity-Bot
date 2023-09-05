from app.server.utils.messages import welcome_menu

def handle_whatsapp_chat():
   try:
       pass
   except:
       pass





opening_inputs = ['hi', 'Hi', 'hello', 'Hello', 'Hey', 'hey']
quit_inputs = ['q', 'Q', 'Quit', 'quit', 'QUIT']
opening_msg = random.choice(opening_inputs).upper()

if text in opening_inputs:
    bot_message = welcome_menu(profile_name, opening_msg)
    send_whatsapp_message(from_id, bot_message)
    schema = {
        "user_phone_number": from_id,
        "user_name": profile_name,
        "created_at": datetime.utcnow()
    }
    new_user_session = await add_user_session(schema)