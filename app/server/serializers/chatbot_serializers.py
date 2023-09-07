# User Sessions Serializer

def user_session_serializer(input) -> dict:
    return {
        "_id": str(input["_id"]),
        "session_id": input["session_id"],
        "user_phone_number": input["user_phone_number"],
        "user_name": input["user_name"],
        "entry_message": input["entry_message"],
        "user_input_1": input["user_input_1"],
        "user_input_2": input["user_input_2"],
        "meter_owner": input["meter_owner"],
        "meter_address": input["meter_address"],
        "meter_package": input["meter_package"],
        "user_meter_number": input["user_meter_number"],
        "user_amount": input["user_amount"],
        "user_confirm": input["user_confirm"],
        "payment_mode": input["payment_mode"],
        "user_order_id": input["user_order_id"],
        "transaction_reference": input["transaction_reference"],
        "created_at": str(input["created_at"]),
        "user_profile": input["user_profile"]
    }

def user_serializer(input) -> dict:
    
    return {
        "_id": str(input["_id"]),
        "username": input["username"],
        "first_name": input["first_name"],
        "email": input["email"],
        "created_at": str(input["created_at"])
    }

def user_profile_serializer(input) -> dict:
    
    return {
        "_id": str(input["_id"]),
        "phone_number": input["phone_number"],
        "phone_id": input["phone_id"],
        "user": input["user"],
        "created_at": str(input["created_at"])
    }

def order_serializer(input) -> dict:
    
    return {
        "_id": str(input["_id"]),
        "user_profile": input["user_profile"],
        "meter_distribution": input["meter_distribution"],
        "user_meter_number": input["user_meter_number"],
        "meter_owner": input["meter_owner"],
        "meter_address": input["meter_address"],
        "meter_package": input["meter_package"],
        "user_amount": input["user_amount"],
        "payment_confirmation": input["payment_confirmation"],
        "unit_confirmation": input["unit_confirmation"],
        "payment_mode": input["payment_mode"],
        "user_order_id": input["user_order_id"],
        "transaction_reference": input["transaction_reference"],
        "created_at": str(input["created_at"])
    }