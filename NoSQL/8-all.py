#!/usr/bin/env python3
"""
A function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """Return a list of all documents in a collection"""
    return mongo_collection.find()
