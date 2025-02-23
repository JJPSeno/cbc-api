from enum import Enum
from typing import Union
from pydantic import BaseModel
from uuid import UUID

################################
#..............................#
#.Eventually need to rewrite...#
#.all the classes here into....#
#.classes in the modals folder.#
#..............................#
################################

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

class CompanyBranches(BaseModel):
  id: UUID
  name: str
  specialty: str
  address: str
  contactNo: str
  description: Union[str, None] = None

class LoginPayload(BaseModel):
  email: str
  password: str