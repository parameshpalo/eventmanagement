from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class CreateEvent(BaseModel):
  event_name : str
  event_date : datetime
  event_location:str


class UpdateEvent(BaseModel):
  event_name : Optional[str] = None
  event_date : Optional[datetime] = None
  event_location: Optional[str] = None

class CreateUser(BaseModel):
  user_name : str
  user_email : str
  password : str

class UserOut(BaseModel):
  user_id : int
  user_name : str

class GuestReg(BaseModel):
  guest_email : str
  guest_name : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

