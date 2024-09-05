from typing import Any, Dict, List
import pymongo
from app.db.Repository import Repository
from app.config import settings
from pymongo.results import InsertOneResult
from pymongo.cursor import Cursor
from pymongo import MongoClient, database

class MongoDBRepository(Repository):
    """This class represents a MongoDB repository which is backed by a MongoDB database.
       Using repositories to access data will allow us to detach models from underlying storage.
       We can use DynamoDB instead of MongoDB in production for scale.
    """
    mongo_client: MongoClient
    db: database.Database
    
    @staticmethod
    def initialize():
        print("Initializing MongoDB " + settings.mongodb_url)
        MongoDBRepository.mongo_client = MongoClient(settings.mongodb_url, maxPoolSize=50)
        MongoDBRepository.db = MongoDBRepository.mongo_client.get_database("ragapi")

    @staticmethod        
    def insertOne(tableOrCollection: str, documentOrRecord: Any) -> InsertOneResult:
        collection = MongoDBRepository.db[tableOrCollection]
        return collection.insert_one(documentOrRecord)

    @staticmethod
    def getAll(tableOrCollection: str, skip: int = 0, limit: int = 0) -> List[Dict[str, Any]]:
        collection = MongoDBRepository.db[tableOrCollection]
        if skip > 0 and limit > 0:
            return list(collection.find().skip(skip).limit(limit))
        elif skip > 0:
            return list(collection.find().skip(skip))
        elif limit > 0:
            return list(collection.find().limit(limit))
        else:
            return list(collection.find())

