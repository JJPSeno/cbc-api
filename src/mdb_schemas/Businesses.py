def serialize_business(business) -> dict:
  return {
    "id": str(business["_id"]),
    "company_name": business["company_name"],
    "address": business["address"],
    "contact_info": {
      "phone_number": business["contact_info"]["phone_number"],
      "email": business["contact_info"].get("email")
    }
  }


def list_businesses(businesses) -> list:
  return[serialize_business(business) for business in businesses]