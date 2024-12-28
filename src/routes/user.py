from fastapi import APIRouter, Header
from typing import Annotated
import jwt
from .auth import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix='/user')

@router.get('/me')
def me(authorization: Annotated[str, Header()]):
  print(authorization)
  details = jwt.decode(authorization, JWT_SECRET_KEY, algorithms=[ALGORITHM])
  print(details)
  return {'message':'Request Recieved', "user": details}