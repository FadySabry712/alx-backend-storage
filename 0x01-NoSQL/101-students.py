#!/usr/bin/env python3
"""
script to return Top students
"""


def top_students(mongo_collection):
    """ returns top students sorted by average score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
