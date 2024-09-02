from pymongo import MongoClient

try:
    client = MongoClient(
        "mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/PD_homework_8?retryWrites=true&w=majority"
    )
    db = client.get_database("PD_homework_8")
    print("Connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")
