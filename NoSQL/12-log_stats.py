#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.logs
    collection = db.nginx
    docs = collection.count_documents({})

    print("{} logs".format(docs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
        filter_path = {"method": method, "path": "/status"}

    print("{} status check".format(collection.count_documents(filter_path)))
