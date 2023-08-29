from emoji import emojize

def welcome_menu(profile_name: str, start_input: str):
    message = f"{start_input}, Nice to Meet Yopu I'm EnergiEase Bot {emojize(':bulb:', language='alias')} from Mind Colony!\nWhat would you like to do today? \n\n{emojize(':one:', language='alias')} Buy Electricity\n{emojize(':two:', language='alias')} Customer Support\n\n Please reply with a number to choose an option(E.g 1 for Buy Electricity)"

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

def 
    