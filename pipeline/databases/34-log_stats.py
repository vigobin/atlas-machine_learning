#!/usr/bin/env python3
"""Log stats:
     script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')

    db = client.logs

    nginx = db.nginx

    num_logs = nginx.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: nginx.count_documents(
            {"method": method}) for method in methods}

    # Get the number of documents with method=GET and path=/status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})

    print(f"{num_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_count} status check")
