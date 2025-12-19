#!/usr/bin/env python3
"""UPDATE TOPICS"""

def update_topics(mongo_collection, name, topics):
    """FUNCTION TO UPDATE TOPICS"""
    
    return mongo_collection.update_many({'name': name}, {"$set": {'topics': topics}})