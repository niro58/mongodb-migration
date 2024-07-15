from os import environ as env
from typing import List

from modules.db import MongoDB
from pymongo import MongoClient
from pymongo.collection import Collection


class Repository:
    connection: MongoClient
    collection: Collection

    def __init__(self, database, collection_name):
        mongo_db = MongoDB()

        self.connection = mongo_db.get_connection()
        self.collection = mongo_db.get_collection(
            database=database,
            collection_name=collection_name
        )

    def move_to(self, b_repo: 'Repository'):
        raise NotImplementedError

    def copy_to(self, b_repo: 'Repository', filter={}, batch_size=10000, max_insert_size=250000):
        repo_size = self.collection.count_documents(filter)

        print(f"Moving {self.collection.name} to {b_repo.collection.name}")
        print(f"Moving {repo_size} documents")
        print(f"Batch size: {batch_size}")

        count = 0
        inserts = []
        while count < repo_size:
            print(f"{count} / {repo_size}")
            res = self.collection.find(filter).skip(count).limit(batch_size)
            inserts += [doc for doc in res]

            if len(inserts) >= max_insert_size:
                print(f"Inserting documents")
                b_repo.collection.insert_many(inserts, ordered=False)
                inserts = []
                print(f"Inserted documents")

            count += batch_size
            repo_size = self.collection.count_documents(filter)

        b_repo.collection.insert_many(inserts, ordered=False)
