import os

from motor.motor_asyncio import AsyncIOMotorClient

from app.db.constants import CONN_STRING


client = AsyncIOMotorClient(CONN_STRING)

db = client["travel_platform"]

def check_connection():
    try:
        client.admin.command("ping")
        print("\n\nMONGO DB connection successful\n\n")
    except Exception as e:
        print("Connection failed due to:", str(e))

def get_db():
    return db

def get_collection(collection_name: str):
    return db[collection_name]

check_connection()