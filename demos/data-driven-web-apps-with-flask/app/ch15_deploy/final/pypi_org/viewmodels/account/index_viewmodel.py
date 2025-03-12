from pypi_org.services import user_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)
