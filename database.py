from fastapi import FastAPI
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

#region load env variables
os.environ.pop("MONGODB_USERNAME", None)
os.environ.pop("MONGODB_PASSWORD", None)
os.environ.pop("MONGODB_CONNECTION_STRING", None)

load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
#endregion

uri = MONGODB_CONNECTION_STRING.replace("<db_username>",MONGODB_USERNAME).replace("<db_password>",MONGODB_PASSWORD)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)