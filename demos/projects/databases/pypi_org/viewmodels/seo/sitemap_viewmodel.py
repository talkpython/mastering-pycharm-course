import flask

from pypi_org.services import package_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class SiteMapViewModel(ViewModelBase):
    def __init__(self, limit: int):
        super().__init__()
        self.packages = package_service.all_packages(limit)
        self.last_updated_text = "2019-07-15"
        self.site = "{}://{}".format(flask.request.scheme, flask.request.host)
