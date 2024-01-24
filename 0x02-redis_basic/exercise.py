#!/usr/bin/env python3
""" Writing strings to redis """
import redis
import uuid
from typing import Union


class Cache:
    """
    A caching class using Redis

    Attributes:
        _redis (redis.Redis): The redis client instance
    """

    def __init__(self):
        """
        Initializes the Cache class with a redis client instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key and stores the input in Redis

        Args:
            data (Union[str, bytes, int, float]): The data to be stored

        Returns:
            str: The randomly generated key used for storage
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
