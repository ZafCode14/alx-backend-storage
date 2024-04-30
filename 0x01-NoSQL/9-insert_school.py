#!/usr/bin/env python3
"""Module with a python script"""


def insert_school(mongo_collection, **kwargs):
    """Incers school"""
    inserted_document = mongo_collection.insert_one(kwargs)
    return inserted_document.inserted_id
