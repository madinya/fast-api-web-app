from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from views import account_router, home_router, packages_router

app = FastAPI()


def configure():
    configure_routers()
    configure_static_files()


def configure_static_files():
    app.mount("/static", StaticFiles(directory="static"), name="static")


def configure_routers():
    app.include_router(home_router)
    app.include_router(account_router)
    app.include_router(packages_router)
