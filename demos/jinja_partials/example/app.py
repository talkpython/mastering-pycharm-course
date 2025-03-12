import flask

import jinja_partials
from views import home

app = flask.Flask(__name__)

app.register_blueprint(home.blueprint)
jinja_partials.register_extensions(app)

if __name__ == '__main__':
    print(f"Running demo app with jinja-partials=={jinja_partials.__version__}.")
    app.run(debug=True, port=5001)
