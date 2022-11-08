from typing import List

from fastapi.requests import Request

from services import package, user
from view_models.shared.view_model_base import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = package.release_count()
        self.user_count: int = user.user_count()
        self.package_count: int = package.package_count()
        self.packages: List = package.latest_packages(limit=5)
