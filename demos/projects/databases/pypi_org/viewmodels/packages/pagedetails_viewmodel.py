from pypi_org.services import user_service, package_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class PackageDetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str):
        super().__init__()
        self.package_name = package_name
        self.package = None
        if package_name:
            self.package_name = package_name.strip().lower()
            self.package = package_service.get_package_by_id(self.package_name)

        self.latest_version = "0.0.0"
        self.latest_release = None
        self.is_latest = True

        if self.package and self.package.releases:
            self.latest_release = self.package.releases[0]
            self.latest_version = self.latest_release.version_text

        self.release_version = self.latest_release
