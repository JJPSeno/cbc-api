from fastapi import APIRouter, Header, Depends, HTTPException, status
from typing import Annotated, Union
from dotenv import load_dotenv
import os

import jwt
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel

load_dotenv()

PW_SECRET_KEY = os.getenv("PW_SECRET_KEY")

if not PW_SECRET_KEY:
  raise ValueError("PW_SECRET_KEY environment variable is not set!")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

if not JWT_SECRET_KEY:
  raise ValueError("JWT_SECRET_KEY environment variable is not set!")

ALGORITHM = os.getenv("ALGORITHM")

if not ALGORITHM:
  raise ValueError("ALGORITHM environment variable is not set!")

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

if not ACCESS_TOKEN_EXPIRE_MINUTES:
  raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES environment variable is not set!")

fake_users_db = {
  "johndoe": {
    "username": "johndoe",
    "full_name": "John Doe",
    "email": "johndoe@example.com",
    "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    "disabled": False,
  }
}

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password using bcrypt
def hash_password(password):
  pwd_bytes = (password + PW_SECRET_KEY).encode('utf-8')
  hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=bcrypt.gensalt())
  return hashed_password

# Check if the provided password matches the stored password (hashed)
def verify_password(plain_password, hashed_password):
  password_byte_enc = (plain_password + PW_SECRET_KEY).encode('utf-8')
  return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)

class RegisterPayload(BaseModel):
  email: str
  password: str
  full_name: Union[str, None] = None

class LoginPayload(BaseModel):
  email: str
  password: str

router = APIRouter(prefix='/auth')

@router.post('/register')
def register(registerPayload: RegisterPayload):
  try:
    print(registerPayload)
    hashed_pwd = hash_password(registerPayload.password)
    print(hashed_pwd)
    fake_users_db[registerPayload.email] = {"email":registerPayload.email, "hashed_password": hashed_pwd}
    return {'message':'Request Recieved'}
  except HTTPException as e:
    raise e

@router.post('/login')
def login(loginPayload: LoginPayload):
  try:
    print(loginPayload)
    user = fake_users_db[loginPayload.email]
    verified_pwd = verify_password(loginPayload.password, user["hashed_password"])
    token = ""
    if verified_pwd is True:
      token = jwt.encode({"email":loginPayload.email}, JWT_SECRET_KEY, ALGORITHM)
    else:
      raise Exception({"message": "Password incorrect"})
    return {'message':'Request Recieved', "token": token}
  except HTTPException as e:
    raise e