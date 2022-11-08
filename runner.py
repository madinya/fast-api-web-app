import uvicorn
from main import configure, app

if __name__ == '__main__':
    configure()
    uvicorn.run("main:app", reload=True)
else:
    configure()
