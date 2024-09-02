from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/")
    db = client.PD_homework_8
    return db
