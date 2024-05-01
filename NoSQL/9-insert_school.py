#!/usr/bin/env python3
"""
A function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
