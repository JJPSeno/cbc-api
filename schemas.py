from enum import Enum
from pydantic import BaseModel

class SpecialtyChoices(Enum):
  PASTRIES = 'pastries'
  NETCAFE = 'netcafe'
  PRINTING = 'printing'

class Branch(BaseModel):
  address: str
  contactNo: str

class Company(BaseModel):
  id: int
  name: str
  specialty: str
  branches: list[Branch] = []

