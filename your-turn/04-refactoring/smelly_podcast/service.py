from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def get_episode(show_id):
    info = episode_data.get(show_id)
    return info


def get_show_id_range():
    latest_show_id = max(episode_data.keys())
    oldest_show_id = min(episode_data.keys())
    return latest_show_id, oldest_show_id


def download_data(url):
    resp = requests.get(url)
    resp.raise_for_status()
    dom = ElementTree.fromstring(resp.text)
    items = dom.findall('channel/item')
    episode_count = len(items)
    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode
