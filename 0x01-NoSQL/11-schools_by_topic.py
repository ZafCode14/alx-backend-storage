#!/usr/bin/env python3
"""Module with a python script"""


def schools_by_topic(mongo_collection, topic):
    """List schools by topic"""
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
