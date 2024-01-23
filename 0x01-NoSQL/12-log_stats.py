#!/usr/bin/env python3
""" Log statistics from a dump file """

from pymongo import MongoClient


def nginx_logs_stats():
    """
    Log the statistics from an nginx dump file
    """
    client = MongoClient('mongodb://localhost:27017')

    # Access the 'logs' database and 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print('{} logs'.format(total_logs))

    # Method statistics
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        count = collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, count))

    # Status logs statistics
    status_logs_count = collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_logs_count))

    # Close connection
    client.close()


if __name__ == '__main__':
    nginx_logs_stats()
