from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime


class UserSessionSchema(BaseModel):
    _id: str = Field(...)
    user_phone_number: str = Field(...)
    user_name: str = Field(...)
    user_phone_id: str = Field(...)
    user_input_1: Optional[str]
    user_input_2: Optional[str]
    user_meter_number: Optional[str]
    user_amount: Optional[str]
    user_confirm: Optional[str]
    user_order_id: Optional[str]
    created_at: Union[datetime, None] = None

class OrdersSchema(BaseModel):
    pass

class UsersSchema(BaseModel):
    pass

class UserProfileSchema(BaseModel):
    pass