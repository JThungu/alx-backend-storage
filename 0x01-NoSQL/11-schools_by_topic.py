#!/usr/bin/env python3
"""
Returns list of schools having a specific topic
mongo_collection will be a pymongo collection object
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
