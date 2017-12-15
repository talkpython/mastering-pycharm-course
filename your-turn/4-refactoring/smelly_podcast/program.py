import random
from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def main():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()

    # DOWNLOAD THE EPISODE DATA
    url = 'https://talkpython.fm/episodes/rss'

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    episode_count = len(dom.findall('channel/item'))

    for idx, item in enumerate(dom.findall('channel/item')):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode

    # GET LATEST SHOW ID
    latest_show_id = max(episode_data.keys())

    print("Working with total of {} episodes".format(latest_show_id))

    # DISPLAY RESULTS
    start = random.randint(90, 110)
    latest_id = max(episode_data.keys())
    end = random.randint(130, latest_id + 1)

    for show_id in range(start, end):
        # GET EPISODE
        info = episode_data.get(show_id)
        print("{}. {}".format(info.show_id, info.title))


if __name__ == '__main__':
    main()
