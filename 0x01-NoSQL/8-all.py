#!/usr/bin/env python3
""" Lists all documents """


def list_all(mongo_collection):
    """ Return a list of all the documents or an empty list
    """
    cursor = mongo_collection.find()

    return [doc for doc in cursor]
