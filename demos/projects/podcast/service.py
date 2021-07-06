from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title, link, date, id')
episodes = {}


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

    print(episodes)
