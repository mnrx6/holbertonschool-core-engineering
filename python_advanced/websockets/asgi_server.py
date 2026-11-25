#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute, Mount
from starlette.staticfiles import StaticFiles


async def homepage(request):
    return FileResponse("index.html")


async def websocket_endpoint(websocket):
    await websocket.accept()
    async for msg in websocket.iter_text():
        await websocket.send_text(msg)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
    Mount("/static", app=StaticFiles(directory="."), name="static"),
])
