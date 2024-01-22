#!/usr/bin/env python3
"""
Changes all topics of a schooll document based on the name
mongo_collection will be the pymongo object
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
