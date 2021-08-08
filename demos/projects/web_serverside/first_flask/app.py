import random

import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    num = random.randint(50, 100)
    return flask.render_template('home/index.html', number=num)


if __name__ == '__main__':
    app.run()
