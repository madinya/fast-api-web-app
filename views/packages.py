from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from view_models import DetailsViewModel

packages_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@packages_router.get("/project/{package_name}", response_class=HTMLResponse)
def index(request: Request, package_name: str):
    vm = DetailsViewModel(request= request, package_name=package_name)
    return templates.TemplateResponse("packages/details.html",
                                      vm.to_dict())
    pass
