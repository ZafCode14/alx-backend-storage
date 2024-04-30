#!/usr/bin/env python3
"""Module with a python script"""


def top_students(mongo_collection):
    """Returns avrage score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
