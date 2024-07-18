import pymongo
from .Repository import Repository
from config import settings

class MongoDBRepository(Repository):
    """This class represents a MongoDB repository which is backed by a MongoDB database.
       Using repositories to access data will allow us to detach models from underlying storage.
       We can use DynamoDB instead of MongoDB in production for scale.
    """
    def __init__(self, mongoUrl):
        print ("Creating MongoDB " + settings.mongoDbUrl)
        self.mongo_client = pymongo.MongoClient(mongoUrl, maxPoolSize=50)

    def insertOne(self, colName, document):
        collection = db[colName]
        return collection.insert_one(document)
        

    def getAll(self, colName):         
        documents = db[colName].find()
        # TODO remove this
        for document in documents:
            print(document)
        return documents    
