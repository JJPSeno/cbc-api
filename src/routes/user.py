from fastapi import APIRouter, Header, HTTPException
from typing import Annotated
from config.database import users_collection
import jwt
from fastapi.encoders import jsonable_encoder
from .auth import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .helper import fake_users_db
from ..models.Users import Businesses, BusinessesPayload, UpdateUsersPayload
from bson import ObjectId

router = APIRouter(prefix='/user')

@router.get('/me')
def me(authorization: Annotated[str, Header()]):
  print(authorization)
  details = jwt.decode(authorization, JWT_SECRET_KEY, algorithms=[ALGORITHM])
  session_email = details["email"]
  return {'message':'Request Recieved', "user": fake_users_db[session_email]}

@router.patch("/users/{user_id}")
def update_business(user_id: str, user_payload: UpdateUsersPayload):
  try:
    # Convert the update payload to a dictionary, excluding None values
    update_data = {k: v for k, v in jsonable_encoder(user_payload, exclude_unset=True).items()}

    # If there's nothing to update, return early
    if not update_data:
      raise HTTPException(status_code=400, detail="No fields provided for update")

    # Perform the update in MongoDB
    result = users_collection.update_one(
      {"_id": ObjectId(user_id)}, {"$set": jsonable_encoder(update_data)}
    )

    # Check if the business was found and updated
    if result.matched_count == 0:
      raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}/businesses")
def get_user_businesses(user_id: str):
  pass


@router.post("/users/{user_id}/businesses/{business_id}")
def add_business_to_user(user_id: str, business_id: str):
  pass


@router.delete("/users/{user_id}/businesses/{business_id}")
def remove_business_from_user(user_id: str, business_id: str):
  pass