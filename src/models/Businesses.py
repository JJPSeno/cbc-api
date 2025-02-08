from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactInformation(BaseModel):
  phone_number: str
  email: Optional[EmailStr] = None

class Businesses(BaseModel):
  company_name: str
  address: str
  contact_info: ContactInformation

class BusinessesPayload(BaseModel):
  company_name: str
  address: str
  phone_number: str
  email: Optional[EmailStr] = None