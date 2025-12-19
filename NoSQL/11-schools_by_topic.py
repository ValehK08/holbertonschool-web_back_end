#!/usr/bin/env python3
"""SCHOOLS BY TOPIC"""

def schools_by_topic(mongo_collection, topic):
    """FUNCTION TO GET SCHOOLS BY TOPIC"""
    
    return mongo_collection.find({"topics": topic})