#!/usr/bin/env python3
"""LOG STATS"""
from pymongo import MongoClient

def log_stats():
    """LOG THE STATS"""
    client = MongoClient()
    db = client.logs
    col = db['nginx']
    doc_counts = col.count_documents({})
    print(f"{doc_counts} logs")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for meth in method:
        print(f"\tmethod {meth}: {col.count_documents({'method': meth})}")
    count = col.count_documents({'method': "GET", "path": "/status"})
    print(f"{count} status check")

if __name__ == "__main__":
    """CALL IT"""
    log_stats()