import fastapi
import uvicorn
import fastapi_chameleon
from view import home
from view import account
from view import packages
from starlette.staticfiles import StaticFiles

app = fastapi.FastAPI()

def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)

def configure():
    configure_template()
    configure_route()

def configure_template():
    fastapi_chameleon.global_init('templates')

def configure_route():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router) 
    app.include_router(account.router) 
    app.include_router(packages.router) 


if __name__ == "__main__":
    main()
else:
    configure()
