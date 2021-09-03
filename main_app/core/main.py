# set relative path
import sys
sys.path.append("..")
# imports
from fastapi import FastAPI, Request
import asyncio
# import core routers
# import routers
from logger.controllers import json_listener
from logger.controllers import json_listener


# create app
app = FastAPI()

# connect routers from core app
# connect routers from subapps
app.include_router(json_listener.router)


@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await call_next(request)
    return response


@app.get("/")
async def index():
    return {"message": "Hello World"}
