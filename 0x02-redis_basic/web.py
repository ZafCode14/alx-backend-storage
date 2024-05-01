#!/usr/bin/env python3
"""Module with a python script"""
from functools import wraps
import redis
import requests
from typing import Callable


redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Function decorator count"""
    @wraps(method)
    def invoker(url) -> str:
        """wrapper for function"""
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Function that gets url content"""
    return requests.get(url).text
