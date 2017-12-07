import functools
from typing import List
import urllib.parse
import requests


@functools.lru_cache()
def search(text: str) -> List[str]:
    # TODO: Evaluate whether to expire the cache...
    url = build_url(text)
    response = perform_search(url)
    results = convert_results(response)

    return results


def build_url(text):
    # format is http://search.talkpython.fm/api/search?q=SEARCH

    encoded = urllib.parse.urlencode({'q': text})
    url = 'http://search.talkpython.fm/api/search?{}'.format(encoded)
    return url


def perform_search(url):
    resp = requests.get(url)
    resp.raise_for_status()

    return resp


def convert_results(response):
    data = response.json()
    return [
        d.get('description')
        for d in data.get('results')
    ]
