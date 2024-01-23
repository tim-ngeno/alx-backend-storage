#!/usr/bin/env python3
""" List all documents in a collection """


def list_all(mongo_collection):
    """
    Returns a list of all documents in a collection

    Args:
        mongo_collection (pymongo object): A collection object
    """
    documents = []
    cursor = mongo_collection.find({})
    for document in cursor:
        documents.append(document)

    return documents
