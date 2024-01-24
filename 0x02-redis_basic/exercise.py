#!/usr/bin/env python3
""" Writing strings to redis """
import redis
import uuid
from typing import Any, Callable, Optional, Union


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

    def get(self, key: str, fn: Optional[Callable[..., Any]] = None) ->\
            Union[str, int, None]:
        """
        Retrieves a value mapped to the key from the redis storage

        Args:
            key (str): The key that maps to the target data
            fn (Callable): A function to convert the data back to the
            desired format

        Returns:
            Union[str, bytes, int, None]: The received data
        """
        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Decodes a byte string received from the Redis storage back to a
        native python string

        Args:
            data (bytes): The byte string to be decoded

        Returns:
            str: The decoded string
        """
        return self.get(key, fn=self._decode_utf8)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves an integer value mapped to the key from redis storage

        Args:
            key (str): The key that maps to the target data

        Returns:
            int: The decoded integer
        """
        data = self.get(key, fn=self._convert_to_int)
        return int(data) if isinstance(data, (int, bytes)) else None

    def _decode_utf8(self, data: bytes) -> str:
        """
        Decodes a byte string received from Redis storage to a string

        Args:
            data (bytes): The byte string to be decoded
        """
        return data.decode('utf-8')

    def _convert_to_int(self, data: bytes) -> int:
        """
        Converts a byte string received from Redis strage to an integer

        data (bytes): The byte string to be converted
        """
        return int(data)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
