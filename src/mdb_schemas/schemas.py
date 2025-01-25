def individual_serializer(user) -> dict:
  return {
    "id": str(user["_id"]),
    "email": user["email"],
    "hashed_password": user["hashed_password"],
    "display_name": user.get("display_name"), 
    "first_name": user.get("first_name"),
    "last_name": user.get("last_name")
  }

def list_serial(users) -> list:
  return[individual_serializer(user) for user in users]