def serialize_user(user) -> dict:
  return {
    "id": str(user["_id"]),
    "email": user["email"],
    "hashed_password": user["hashed_password"],
    "display_name": user.get("display_name"), 
    "first_name": user.get("first_name"),
    "last_name": user.get("last_name")
  }

def list_users(users) -> list:
  return[serialize_user(user) for user in users]