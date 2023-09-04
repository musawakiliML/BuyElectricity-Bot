from emoji import emojize

def welcome_menu(profile_name: str, start_input: str):
    message = f"{start_input}, {profile_name} Nice to Meet You, I'm EnergiEase Bot {emojize(':bulb:', language='alias')} from Mind Colony!\nWhat would you like to do today? \n\n{emojize(':one:', language='alias')} Buy Electricity\n{emojize(':two:', language='alias')} Customer Support\n\n Please reply with a number to choose an option(E.g 1 for Buy Electricity)"

    return message

def options_menu():
    message = f"That's perfect!! {emojize(':thumbsup:', language='alias')} Choose from the Distribution Companies available below:\n\n{emojize(':one:', language='alias')} AEDC\n{emojize(':two:', language='alias')} EEDC\n{emojize(':three:', language='alias')} EKEDC\n{emojize(':four:', language='alias')} IBEDCO\n{emojize(':five:', language='alias')} IE\n{emojize(':six:', language='alias')} JED\n{emojize(':seven:', language='alias')} KAEDCO\n{emojize(':eight:', language='alias')} KEDCO\n{emojize(':nine:', language='alias')} PHED\n\n Please reply with a number to choose an option(E.g 1 for AEDC)"

    return message

def meter_number():
    message = f"Please enter your meter number {emojize(':pager:', language='alias')}:"

    return message

def bill_amount():
    message = f"Great! how much {emojize(':battery:', language='alias')} electricity unit (in naira) do you want to buy {emojize(':dollar:', language='alias')}?\n\n {emojize(':heavy_exclamation_mark:', language='alias')} Note: \n\n The minimun order amount should be N1000.0\nA service fee of N100 will be added to the amount."

    return message

def order_summary(owner: str, amount: int, meter_number: str, package: str, address: str):
    message = f"Hurray!, Here is your order summary:\n\n Meter Owner: {owner}\nMeter No: {meter_number}\nAddress: {address}\nPackage: {package}\n\n Amount {emojize(':dollar:', language='alias')}: N {amount}\n Service Fee: N 100\n\n{emojize(':one:', language='alias')} Confirm Order\n\n To Confirm order please reply with 1."

    return message

def order_payment(amount: str, account_number: int, account_name: str, bank_name: str):
    message = f"Fabulous!! Please send [{amount}] to:\nAccount number: {account_number}\nAccount name: {account_name}\nBank name: {bank_name}\nYour request would be processed automatically once we recieved your payment."

    return message

def order_confirmation(order_id: str):
    message = f"Fantastic!! Your order has been recieved.\nOrder Id:{order_id} \n We are processing it."

    return message

def order_successful(meter_unit: str, order_id: str, meter_number: str, meter_token: str):
    message = f"Your Order was successful!!\n You can get the details below:\n\nToken:{meter_token}\nOrder Id: {order_id}\nUnits: {meter_unit}\nMeter Number: {meter_number}\n\nThank you for choosing EnergiEase!"

    return message

def order_failed(order_id: str):
    message = f"OOPs Your order has failed!!\n Please Contact Support through email with your Order Id:{order_id}. support@energieasebot.ng"
    