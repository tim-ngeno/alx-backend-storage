#!/usr/bin/env python3
""" Update topics based by name """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection (pymongo object): A mongo collection
        name (str): the school name to update
        topics (list[str]): topics approached in the school
    """
    result = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

    return result.modified_count
