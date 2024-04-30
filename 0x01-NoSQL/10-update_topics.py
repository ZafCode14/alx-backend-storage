#!/usr/bin/env python3
"""Module with a python script"""


def update_topics(mongo_collection, name, topics):
    """Updates topics"""
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
