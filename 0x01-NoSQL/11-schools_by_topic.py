#!/usr/bin/env python3
""" Module for using PyMongo to retrieve spesfic topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a said topic """
    return mongo_collection.find({"topics": topic})
