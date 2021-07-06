from collections import namedtuple
from typing import Optional, Dict
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title, link, date, id')
episodes: Dict[int, Episode] = {}


def download_info():
    url = 'https://talkpython.fm/episodes/rss'

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')

    for idx, item in enumerate(items, start=0):
        e = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            len(items) - idx - 1
        )

        episodes[e.id] = e


def get_min_episode_id() -> int:
    return min(episodes.keys())


def get_max_episode_id() -> int:
    return max(episodes.keys())


def get_details(episode_id) -> Optional[Episode]:
    return episodes.get(episode_id)
