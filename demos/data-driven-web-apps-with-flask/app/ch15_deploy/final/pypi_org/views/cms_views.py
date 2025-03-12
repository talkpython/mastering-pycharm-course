import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.viewmodels.cms.page_viewmodel import PageViewModel

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    vm = PageViewModel(full_url)

    if not vm.page:
        return flask.abort(404)

    return vm.to_dict()
