#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """function that lists all documents in a collection.
        Return an empty list if no document in the collection
        mongo_collection will be the pymongo collection object."""
    documents = mongo_collection.find()
    return documents
