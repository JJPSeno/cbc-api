from fastapi import APIRouter, Header, HTTPException
from typing import Annotated
import jwt
from .auth import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .helper import fake_companies_db
from ..schemas.schemas import Company, SpecialtyChoices

router = APIRouter()

@router.get('/companies')
async def companies() -> list[Company]:
  return [
    Company(**c) for c in fake_companies_db
  ]

@router.get('/companies/{id}')
async def company(id: int) -> Company:
  company = next((Company(**c) for c in fake_companies_db if c['id'] == id), None)
  if company == None:
    raise HTTPException(status_code=404, detail='company not found')
  return company

@router.get('/companies/specialty/{specialty}')
async def companies_in_specialty(specialty: SpecialtyChoices) -> list[dict]:
  return[
    c for c in fake_companies_db if c['specialty'].lower() == specialty.value
  ]