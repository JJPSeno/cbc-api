from fastapi import APIRouter, Header
from typing import Annotated

router = APIRouter(prefix='/auth')

@router.post('/register')
def register(body):
  return {'message':'Request Recieved'}

@router.post('/login')
def login(body):
  return {'message':'Request Recieved'}