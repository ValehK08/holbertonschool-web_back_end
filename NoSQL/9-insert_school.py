#!/usr/bin/env python3
"""INSERT SCHOOL"""

def insert_school(mongo_collection, **kwargs):
    """FUNCTION TO INSERT SCHOOL"""
    
    return mongo_collection.insertOne(kwargs).inserted_id