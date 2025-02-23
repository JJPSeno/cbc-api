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
from ..models.Businesses import Businesses, BusinessesPayload, UpdateBusinessesPayload
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

@router.patch("/businesses/{business_id}")
def update_business(business_id: str, business_payload: UpdateBusinessesPayload):
  try:
    # Convert the update payload to a dictionary, excluding None values
    update_data = {k: v for k, v in jsonable_encoder(business_payload, exclude_unset=True).items()}

    # If there are updates related to `contact_info`, restructure them properly
    contact_info_fields = ["phone_number", "email"]
    contact_info_update = {k: update_data.pop(k) for k in contact_info_fields if k in update_data}
    
    if contact_info_update:
      update_data["contact_info"] = contact_info_update

    # If there's nothing to update, return early
    if not update_data:
      raise HTTPException(status_code=400, detail="No fields provided for update")

    # Perform the update in MongoDB
    result = businesses_collection.update_one(
      {"_id": ObjectId(business_id)}, {"$set": jsonable_encoder(update_data)}
    )

    # Check if the business was found and updated
    if result.matched_count == 0:
      raise HTTPException(status_code=404, detail="Business not found")

    return {"message": "Business updated successfully"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.get('/businesses')
def get_businesses():
  try:
    businesses = list_businesses(businesses_collection.find())
    return businesses
  except HTTPException as e:
    raise e