from fastapi import APIRouter, Header, Depends, HTTPException, status
from typing import Annotated, Union
from dotenv import load_dotenv
import os

import jwt
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from jwt.exceptions import InvalidTokenError
from config.database import businesses_collection
from ..mdb_schemas.Businesses import list_businesses, serialize_business
from ..models.Businesses import Businesses, ContactInformation, BusinessesPayload
from bson import ObjectId

router = APIRouter(prefix='/businesses')


@router.post('/businesses')
def new_businesses(business_payload: BusinessesPayload):
  try:
    contact_info = {"phone_number": business_payload.phone_number, "email": business_payload.email }
    businesses_data = {"company_name": business_payload.company_name, "address": business_payload.address, "contact_info": contact_info}
    businesses = Businesses.model_validate(businesses_data)
    businesses_collection.insert_one(jsonable_encoder(businesses))
    return  {'message':'Request Recieved'}
  except HTTPException as e:
    raise e


@router.get('/businesses')
def get_businesses():
  try:
    businesses = list_businesses(businesses_collection.find())
    return businesses
  except HTTPException as e:
    raise e