import json
from pathlib import Path
from typing import List, Dict

from models.category_model import Category
from models.video_model import Video

__categories: Dict['str', Category] = {}
__all_videos_list: List[Video] = []


def load_data():
    global __all_videos_list, __categories
    if __all_videos_list:
        return

    __categories = {}
    __all_videos_list = []

    file = Path(__file__).parent.parent / 'db' / 'videos.json'
    with open(file, 'r') as fin:
        data = json.load(fin)

    categories = [
        Category(**category)
        for category in data
    ]

    for c in categories:
        __categories[c.category.lower().strip()] = c
        for v in c.videos:
            v.category = c.category

    rebuild_flat_file_list()


def rebuild_flat_file_list():
    global __all_videos_list

    flat_set = {
        v.id: v
        for cat_name, cat in __categories.items()
        for v in cat.videos
    }
    __all_videos_list = list(flat_set.values())
    __all_videos_list.sort(key=lambda vid: vid.views, reverse=True)


def all_videos() -> List[Video]:
    load_data()
    return list(__all_videos_list)


def top_videos(count: int = 3) -> List[Video]:
    load_data()
    return all_videos()[:count]
