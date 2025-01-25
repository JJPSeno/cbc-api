from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.pop("MONGODB_USERNAME", None)
os.environ.pop("MONGODB_PASSWORD", None)
os.environ.pop("MONGODB_CONNECTION_STRING", None)

load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")

uri = MONGODB_CONNECTION_STRING.replace("<db_username>",MONGODB_USERNAME).replace("<db_password>",MONGODB_PASSWORD)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.cbcdb

users_collection = db["cbcdb_users"]