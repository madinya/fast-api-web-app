from fastapi import Request
from view_models import ViewModelBase
from models.user import User


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('Roberto', 'rmadinya@mad.com', '9hsdhhsy74s')
