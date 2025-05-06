#!/usr/bin/env python3
""" Module for using PyMongo to insert documents """


def insert_school(mongo_collection, **kwargs):
    """ Inserts new document in a collection based on kwargs """
    id_obj = mongo_collection.insert_one(kwargs)

    return id_obj.inserted_id
