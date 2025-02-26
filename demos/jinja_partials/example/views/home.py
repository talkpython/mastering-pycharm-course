import flask  # noqa

from services import video_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.get('/')
def index():
    row1 = video_service.top_videos()



    rows = [row1]
    return flask.render_template('home/index.html', rows=rows)


@blueprint.get('/listing')
def listing():
    videos = video_service.all_videos()
    return flask.render_template('home/listing.html', videos=videos)
