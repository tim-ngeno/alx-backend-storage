#!/usr/bin/env python3
""" Returns a list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        mongo_collection (pymongo object): A mongo collection
        topic (str): the input topic to be searched
    """
    result = mongo_collection.find({'topics': topic})
    return list(result)
