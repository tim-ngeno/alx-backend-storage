#!/usr/bin/env python3
""" expiring web cache and tracker """

import requests
import time
from functools import wraps
from typing import Callable, Optional

# Simulating a cache (you might want to use a proper caching mechanism)
cache_data = {}


def cache_set(key: str, value: str, expiration_time: int) -> None:
    """
    Set a value in the cache with an expiration time.

    Args:
        key (str): The key for the cache entry.
        value (str): The value to be cached.
        expiration_time (int): The expiration time for the cache entry.
    """
    cache_data[key] = {
        'value': value,
        'expiration_time': time.time() + expiration_time
    }


def cache_get(key: str) -> Optional[str]:
    """
    Get a value from the cache.

    Args:
        key (str): The key for the cache entry.

    Returns:
        Optional[str]: The cached value, or None if not found or expired.
    """
    if key in cache_data:
        if cache_data[key]['expiration_time'] > time.time():
            return cache_data[key]['value']
        else:
            del cache_data[key]
    return None


def cache_increment(key: str) -> None:
    """
    Increment the count for a key in the cache.

    Args:
        key (str): The key for the count entry in the cache.
    """
    cache_data[key] = cache_data.get(key, 0) + 1


def cache_with_count(expiration_time: int = 10) -> Callable:
    """
    Decorator to cache function results and count access.

    Args:
        expiration_time (int): The expiration time for the cache entries.

    Returns:
        Callable: The decorated function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            count_key = f"count:{url}"
            page_key = f"page:{url}"

            # Check if the page is already cached
            cached_page = cache_get(page_key)
            if cached_page:
                return cached_page

            # If not cached, fetch the page and update count
            response = func(url)
            cache_set(page_key, response, expiration_time)
            cache_increment(count_key)

            return response

        return wrapper

    return decorator


@cache_with_count()
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL, caching and counting access.

    Args:
        url (str): The URL for which to fetch the HTML content.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"

    # First call (not cached)
    print(get_page(url))

    # Second call (cached)
    print(get_page(url))

    # Third call after cache expiration (not cached)
    time.sleep(11)
    print(get_page(url))
