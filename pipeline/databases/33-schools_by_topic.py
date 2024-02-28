#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic:
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched."""
    schools = mongo_collection.find({"topics": topic})
    return [school for school in schools]
