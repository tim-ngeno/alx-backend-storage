#!/usr/bin/env python3
""" Orders all students sorted by average score """


def top_students(mongo_collection):
    """
    Returns all the students sorted by average score

    Args:
        mongo_collection (pymongo object): A pymongo collection object
    """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'topics': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
