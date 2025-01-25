from pydantic import BaseModel, EmailStr
from typing import Optional

class Users(BaseModel):
  email: EmailStr
  hashed_password: str
  display_name: str
  first_name: Optional[str] = None
  last_name: Optional[str] = None

class RegisterPayload(BaseModel):
  email: EmailStr
  password: str
  display_name: str
  first_name: Optional[str] = None
  last_name: Optional[str] = None
