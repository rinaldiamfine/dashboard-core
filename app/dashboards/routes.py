from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

DashboardRoute = APIRouter()

websites = Jinja2Templates(directory="app/templates")

@DashboardRoute.get("/dashboard", response_class=HTMLResponse, tags=['Dashboards'])
async def website_dashboard(request: Request):
    '''Dashboard View'''
    return websites.TemplateResponse("dashboard.html", {"request": request})