from os import environ as env

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.mongo_client import MongoClient


class MongoDB:
    _instance = None
    client: MongoClient

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)

            uri = env.get("MONGO_CONNECTION")
            assert uri is not None, "MONGO_CONNECTION is not set in the environment variables."

            cls._instance.client = MongoClient(uri)
            try:
                cls._instance.client.server_info()
            except Exception:
                raise Exception("MongoDB connection failed")

        return cls._instance

    def get_connection(self) -> MongoClient:
        return self.client

    def get_collection(self, database, collection_name) -> Collection:
        assert database in self.client.list_database_names(
        ), f"{database} not found in the database."
        assert collection_name in self.client[database].list_collection_names(
        ), f"{collection_name} not found in the database."
        return self.client[database][collection_name]
