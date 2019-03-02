# This program requires Python 3.6+
#
# * get stopwords
# * get positive words
# * get negative words
# * get corpus
# * score = (count positive - count negative) / (num words)
#   bounds [-1, 1]
#
import os
import re
import time
import urllib

import requests

BASE = 'https://raw.githubusercontent.com/jeffreybreen/' \
       'twitter-sentiment-analysis-tutorial-201107/master/' \
       'data/opinion-lexicon-English/'
NEG_URL = f'{BASE}negative-words.txt'
POS_URL = f'{BASE}positive-words.txt'

STOPWORDS_URL = 'https://raw.githubusercontent.com/' \
                'stanfordnlp/CoreNLP/master/data/edu/stanford/nlp/' \
                'patterns/surface/stopwords.txt'


def main():
    get_url(NEG_URL, 'neg.txt')
    get_url(POS_URL, 'pos.txt')
    get_url(STOPWORDS_URL, 'stop.txt')
    posts = get_posts('numpy')

    for post in posts:
        words = get_line_words([post['description']])
        print(f"{post['title'][:20]:20} Score: {get_score(words):6.3f}")


def get_url(url, filename):
    if os.path.exists(filename):
        return
    fin = requests.get(url)
    data = fin.text

    # noinspection SpellCheckingInspection
    with open(filename, 'w') as fout:
        fout.write(data)


def get_line_words(fin):
    r"""
    >>> get_line_words([': ."hello world, my name!\n', 'is matt.\n'])
    ['world', 'my', 'name', 'is', 'matt']
    """
    book_words = []
    word_re = re.compile(r'(\w*)')

    for line in fin:
        for word in line.split():
            # don't use match it checks start of line
            valid = word_re.search(word)
            if valid and valid.group(1):
                book_words.append(valid.group(1))
    return book_words


def get_posts(query):
    # noinspection PyUnresolvedReferences
    enc = urllib.parse.urlencode({'q': query})
    url = f'http://search.talkpython.fm/api/search?{enc}'
    res = requests.get(url)
    return [d for d in res.json().get('results')]


def get_score(words):
    print("Processing {} words".format(len(words)))
    if not len(words):
        return 0.0

    neg = [line.lower().strip() for line in open('neg.txt')]
    pos = [line.lower().strip() for line in open('pos.txt')]
    stop = [line.lower().strip() for line in open('stop.txt')]

    p_count = 0
    n_count = 0
    remove = 0
    for word in words:
        if word in stop:
            remove += 1
            continue
        if word in pos:
            p_count += 1
        if word in neg:
            n_count += 1

    score = (p_count - n_count) / (len(words) - remove)
    return score


if __name__ == '__main__':
    print("Calculating sentiment on episodes...", flush=True)

    start = time.time()

    main()

    print(f"\ntook {time.time() - start:.3} seconds")
