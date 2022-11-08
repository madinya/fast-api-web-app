from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from view_models import IndexViewModel, ViewModelBase

home_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_router.get("/", response_class=HTMLResponse)
async def home(request: Request, id: int = 1):
    vm = IndexViewModel(request=request)
    return templates.TemplateResponse("home/index.html",
                                      vm.to_dict())


@home_router.get("/about", response_class=HTMLResponse)
async def home(request: Request):
    vm = ViewModelBase(request)
    return templates.TemplateResponse("home/about.html",
                                      vm.to_dict())
