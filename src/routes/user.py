from fastapi import APIRouter, Header
from typing import Annotated

router = APIRouter(prefix='/user')

@router.get('/me')
def me(authorization: Annotated[str, Header()]):
  print(authorization)
  return {'message':'Request Recieved'}