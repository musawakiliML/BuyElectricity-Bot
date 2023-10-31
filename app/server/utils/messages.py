from emoji import emojize

def welcome_menu(profile_name: str, start_input: str):
    message = f"{start_input}, {profile_name} Nice to Meet You, I'm EnergiEase Bot {emojize(':bulb:', language='alias')} from Mind Colony!\nWhat would you like to do today? \n\n{emojize(':one:', language='alias')} Buy Electricity⚡\n{emojize(':two:', language='alias')} Customer Support ☎️\n\n Please reply with a number to choose an option(E.g 1 for Buy Electricity)"

    return message

def options_menu():
    message = f"That's perfect!! {emojize(':thumbsup:', language='alias')} Choose from the Distribution Companies available below:\n\n{emojize(':one:', language='alias')} AEDC\n{emojize(':two:', language='alias')} EEDC\n{emojize(':three:', language='alias')} EKEDC\n{emojize(':four:', language='alias')} IBEDCO\n{emojize(':five:', language='alias')} IKEDC\n{emojize(':six:', language='alias')} JED\n{emojize(':seven:', language='alias')} KAEDCO\n{emojize(':eight:', language='alias')} KEDCO\n{emojize(':nine:', language='alias')} PHED\n{emojize(':ten:', language='alias')}BEDC\n\n Please reply with a number to choose an option(E.g 1 for AEDC)"

    return message

def meter_number_menu():
    message = f"Please enter your meter number {emojize(':pager:', language='alias')}:"

    return message

def meter_type_menu():
    message = f"Please Select Your Meter Type:\n{emojize(':one:', language='alias')} Prepaid\n{emojize(':two:', language='alias')} Postpaid"
    return message

def bill_amount_menu():
    message = f"Great! how much {emojize(':battery:', language='alias')} electricity unit (in naira) do you want to buy {emojize(':dollar:', language='alias')}?\n\n{emojize(':heavy_exclamation_mark:', language='alias')}Note: The minimun order amount should be N1000.0\nA service fee of N100 will be added to the amount."

    return message

def order_summary(owner: str, amount: str, meter_number: str, package: str, address: str):
    message = f"Hurray!, Here is your order summary:\n\n\t👤 Meter Owner:{owner}\n\t🔢 Meter No: {meter_number}\n\t📍 Address: {address}\n\t📦 Package: {package}\n\n\t💵 Amount {emojize(':dollar:', language='alias')}: ₦ {amount}\n\tService Fee: ₦ 100\n\n{emojize(':one:', language='alias')} Confirm Order ✔️ \n\n{emojize(':two:', language='alias')} Cancel Order ❌ \n\n To Confirm order please reply with 1."

    return message

def order_payment(amount: str, account_number: int, account_name: str, bank_name: str):
    message = f"Fabulous!! Please send 💵 {amount} to:\n\n\tAccount number: {account_number}\n\tAccount name: {account_name}\n\tBank name: {bank_name}\n\n ⌛ Your request would be processed automatically once we recieved your payment."

    return message

def order_confirmation(order_id: str):
    message = f"Fantastic!! Your order has been recieved.✅\n\n\tOrder Id:*{order_id}*\n⌛ We are processing it."

    return message

def order_successful(meter_unit: str, meter_number: str, meter_token: str):
    message = f"Your Order was successful!! 🎉\n You can get the details below:\n\n\tToken: *{meter_token}*\n\tUnits: *{meter_unit}*\n\tMeter Number: {meter_number}\n\nThank you for choosing EnergiEase!🤗"

    return message

def order_failed(order_id: str):
    message = f"OOPs ❌ Your order has failed!!\n Please Contact Support through email with your Order Id:*{order_id}*. support@energieasebot.ng"
    return message

def customer_support():
    message = f"Welcome to Customer Support. Please Whats your issue Today? Write to us.."
    return message

def quit_chat():
    bot_reply = "Thank You For the using the Bot 🤗, See you next time 👋. Just type 'Hey' 👋To start a conversation."
    return bot_reply


# {'code': '000', 'content': {'transactions': {'status': 'delivered', 'product_name': 'Abuja Electricity Distribution Company- AEDC', 'unique_element': '1111111111111', 'unit_price': 1000, 'quantity': 1, 'service_verification': None, 'channel': 'api', 'commission': 15, 'total_amount': 985, 'discount': None, 'type': 'Electricity Bill', 'email': 'musaadamuw@gmail.com', 'phone': '+2348135810804', 'name': None, 'convinience_fee': 0, 'amount': 1000, 'platform': 'api', 'method': 'api', 'transactionId': '16985959741595911533696844'}}, 'response_description': 'TRANSACTION SUCCESSFUL', 'requestId': '20231029171226e21280d843', 'amount': '1000.00', 'transaction_date': {'date': '2023-10-29 17:12:54.000000', 'timezone_type': 3, 'timezone': 'Africa/Lagos'}, 'purchased_code': 'Token : 3359-3176-5478-0062-9598', 'MeterNumber': '04177505726', 'Token': '3359-3176-5478-0062-9598', 'ReceiptNumber': '7011202109137170448', 'PurchasedUnits': 89.9, 'DebtDescription': None, 'DebtAmount': None, 'RefundUnits': None, 'ServiceChargeVatExcl': None, 'Name': 'DOMINIC Gabriel ', 'Address': 'JABI JABI ABUJA Und St. Vendors Center', 'Reference': 'T21256131638cd89c5bf9b944168837a', 'Vat': 348.84, 'ResponseTime': '9/13/2021 1:16:44 PM', 'TariffRate': '89.9 KWH @ 51.75', 'FreeUnits': None, 'MeterCategory': 'Tariff Band A Non MD'}




{'code': '000', 'content': {'transactions': {'status': 'delivered', 'product_name': 'Jos Electric - JED', 'unique_element': '1111111111111', 'unit_price': 1000, 'quantity': 1, 'service_verification': None, 'channel': 'api', 'commission': 12, 'total_amount': 988, 'discount': None, 'type': 'Electricity Bill', 'email': 'musaadamuw@gmail.com', 'phone': '+2348135810804', 'name': None, 'convinience_fee': 0, 'amount': 1000, 'platform': 'api', 'method': 'api', 'transactionId': '16986165776981317179370057'}}, 'response_description': 'TRANSACTION SUCCESSFUL', 'requestId': '20231029225643e8671dcb8d', 'amount': '1000.00', 'transaction_date': {'date': '2023-10-29 22:56:17.000000', 'timezone_type': 3, 'timezone': 'Africa/Lagos'}, 'purchased_code': 'Token : 5597-5859-9066-3420-0216', 'CustomerName': 'Testmeter1', 'CustomerAddress': 'Test street off military zone', 'DebtTax': None, 'DebtAmount': None, 'DebtValue': None, 'DebtRem': None, 'FixedTax': None, 'FixedAmount': None, 'FixedValue': None, 'Amount': '500', 'Tax': '34.883720930233', 'Units': '13.8', 'Token': '5597-5859-9066-3420-0216', 'Tariff': None, 'Description': None, 'Receipt': '547953438553644936'}