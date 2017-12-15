from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def get_episode(show_id):
    # GET EPISODE
    return episode_data.get(show_id)


def get_latest_show_id():
    # GET LATEST SHOW ID
    return max(episode_data.keys())


def download_data():
    # DOWNLOAD THE EPISODE DATA
    url = 'https://talkpython.fm/episodes/rss'
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
