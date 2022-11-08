from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from infrastructure import cookie_auth
from services import user as user_service
from view_models import RegisterViewModel, LoginViewModel, AccountViewModel

account_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@account_router.get("/account", response_class=HTMLResponse)
async def index(request: Request):
    vm = AccountViewModel(request=request)
    return templates.TemplateResponse("account/index.html",
                                      vm.to_dict())


@account_router.get("/account/register", response_class=HTMLResponse)
async def register(request: Request):
    vm = RegisterViewModel(request=request)
    return templates.TemplateResponse("account/register.html",
                                      vm.to_dict())


@account_router.get("/account/login", response_class=HTMLResponse)
async def login(request: Request):
    vm = LoginViewModel(request=request)
    return templates.TemplateResponse("account/login.html",
                                      vm.to_dict())


@account_router.get("/account/logout")
async def logout(request: Request):
    response = RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response


@account_router.post('/account/register', response_class=HTMLResponse)
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return templates.TemplateResponse("account/register.html",
                                          vm.to_dict())

    # Create the account
    account = user_service.create_account(vm.name, vm.email, vm.password)

    # Login user
    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)

    return response


@account_router.post('/account/login')
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return templates.TemplateResponse("account/login.html",
                                          vm.to_dict())

    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = "The account does not exist or the password is wrong."
        return templates.TemplateResponse("account/login.html",
                                          vm.to_dict())

    resp = RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp
