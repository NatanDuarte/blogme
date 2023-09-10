import pymongo
import os

from dotenv import load_dotenv
load_dotenv()


def get_database_collection(database="", collection=""):
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    uri = f'mongodb://{username}:{password}@{host}:{port}/?authMechanism=DEFAULT&authSource=blog'

    try:
        client = pymongo.MongoClient(uri)
        db = client[database]
        collection = db[collection]

        return collection
    except Exception as e:
        print(f'MongoDB connection failed: {str(e)}')
        return None
