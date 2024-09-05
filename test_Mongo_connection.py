from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client.get_database("PD_homework_8")
    print("Connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")
