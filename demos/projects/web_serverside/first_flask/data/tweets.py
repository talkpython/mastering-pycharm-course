import json
from typing import List


class Tweet:

    def __init__(self, name: str, text: str):
        self.text = text
        self.name = name

    @classmethod
    def load(cls) -> List["Tweet"]:
        with open('data/tweet_stream.json', 'r', encoding='utf-8') as fin:
            data = json.load(fin)

        return [Tweet(**t) for t in data]
