#!/usr/bin/env python3
"""LIST ALL"""

def list_all(mongo_collection):
    """FUNCTION TO LIST ALL"""
    return mongo_collection.find()