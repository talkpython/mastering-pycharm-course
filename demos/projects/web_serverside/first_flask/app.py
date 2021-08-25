import random

import flask
from flask import Flask
from data.tweets import Tweet

app = Flask(__name__)


@app.route('/')
def index():
    num = random.randint(50, 100)
    return flask.render_template('home/index.html', number=num)


@app.route('/tweets')
def tweets():
    recent_tweets = Tweet.load()
    return flask.render_template('home/tweets.html', recent_tweets=recent_tweets)


if __name__ == '__main__':
    app.run()
