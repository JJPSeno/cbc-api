from fastapi import APIRouter, Header
from typing import Annotated
import jwt
from .auth import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .helper import fake_users_db

router = APIRouter(prefix='/user')

@router.get('/me')
def me(authorization: Annotated[str, Header()]):
  print(authorization)
  details = jwt.decode(authorization, JWT_SECRET_KEY, algorithms=[ALGORITHM])
  session_email = details["email"]
  return {'message':'Request Recieved', "user": fake_users_db[session_email]}