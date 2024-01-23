#!/usr/bin/env python3
""" Insert a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection

    Args:
        mongo_collection (pymongo object): A mongo collection
        kwargs (dict): document parameters
    """

    # Insert a new document into the collection based on kwargs
    result = mongo_collection.insert_one(kwargs)

    # Returns the _id of the newly inserted document
    return result.inserted_id
