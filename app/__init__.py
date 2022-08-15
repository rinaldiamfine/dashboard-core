from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import config
import app.metadata as metadatas
import json
from app.tools.socket import socket

app = FastAPI(openapi_tags=metadatas.tags_metadata)
app_socket = socket
configuration = config

app.mount("/packages", StaticFiles(directory="app/packages"), name="packages")

from app.dashboards.routes import DashboardRoute

@app.websocket("/socket/dashboard")
async def websocket_dashboard(websocket: WebSocket):
    """
    Websocket for dashboard
    """
    model = "dashboard"
    index_id = 0
    await app_socket.connect(websocket, model, index_id)
    try:
        while True:
            data = await websocket.receive_text()
            data_obj = json.loads(data)
            print(data_obj, "DATA OBJECT")
            if data_obj.get("type") == "fetch":
                print("FETCH")
                await app_socket.send_data(data_obj, index_id)
            elif data_obj.get("type") == "connect":
                print("CONNECT")
                await app_socket.send_data(data_obj, index_id)
            # await app_socket.send(data_obj, index_id)
            
    except WebSocketDisconnect:
        app_socket.disconnect(websocket, index_id)

app.include_router(DashboardRoute)