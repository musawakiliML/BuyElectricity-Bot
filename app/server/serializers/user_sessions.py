# User Sessions Serializer

def user_session_serializer(input) -> dict:
    return {
        "_id": str(input["_id"]),
        "user_phone_number": input["user_phone_number"],
        "user_name": input["user_name"],
        # "message_id": input["message_id"],
        "user_input_1": input["user_input_1"],
        "user_input_2": input["user_input_2"],
        "user_meter_number": input["user_meter_number"],
        "user_amount": input["user_amount"],
        "user_confirm": input["user_confirm"],
        "user_order_id": input["user_order_id"],
        "created_at": str(input["created_at"])
    }