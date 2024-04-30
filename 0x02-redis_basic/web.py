#!/usr/bin/env python3
"""Module with a python script"""

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Function decorator count"""
    @wraps(method)
    def wrapper(url):
        """wrapper for function"""
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Function that gets url content"""
    req = requests.get(url)
    return req.text
