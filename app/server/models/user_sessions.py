from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime

class UserSchema(BaseModel):
    _id: str = Field(...)
    username: str = Field(...)
    first_name: str = Field(...)
    email: str = Field(...)
    created_at: Union[datetime, None] = None

class UserProfileSchema(BaseModel):
    _id: str = Field(...)
    phone_number: str = Field(...)
    phone_id: str = Field(...)
    user: UserSchema
    created_at: Union[datetime, None] = None

class OrdersSchema(BaseModel):
    _id: str = Field(...)
    user_profile: UserProfileSchema
    meter_distrubution: Optional[str]
    user_meter_number: Optional[str]
    user_amount: Optional[str]
    payment_confirmation: Optional[str]
    unit_confirmation: Optional[str]
    payment_mode: Optional[str]
    user_order_id: Optional[str]
    transaction_reference: Optional[str]

class UserSessionSchema(BaseModel):
    _id: str = Field(...)
    session_id: str = Field(...)
    user_phone_number: str = Field(...)
    user_name: str = Field(...)
    entry_message: Optional[str]
    user_input_1: Optional[str]
    user_input_2: Optional[str]
    user_meter_number: Optional[str]
    user_amount: Optional[str]
    user_confirm: Optional[str]
    payment_mode: Optional[str]
    user_order_id: Optional[str]
    transaction_reference: Optional[str]
    created_at: Union[datetime, None] = None
    user: UserSchema

