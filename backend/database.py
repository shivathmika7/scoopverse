import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "scoopverse")

if not MONGO_URL:
    raise ValueError("MONGO_URL is missing from .env")

client = MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=5000
)

# Test MongoDB connection
client.admin.command("ping")

db = client[DATABASE_NAME]

products_collection = db["products"]
users_collection = db["users"]
orders_collection = db["orders"]

print("MongoDB Connected Successfully!")
