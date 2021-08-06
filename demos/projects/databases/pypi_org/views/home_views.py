import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.viewmodels.home.index_viewmodel import IndexViewModel
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    vm = ViewModelBase()
    return vm.to_dict()
