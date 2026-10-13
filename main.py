from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(
    title="MSA English Test",
    description="Computer-Based English Testing System for Shalahuddin Al-Ayyuby Schools",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/health")
def health():
    return {"status": "ok", "app": "MSA English Test"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "app_name": "MSA English Test",
            "school_name": "Shalahuddin Al-Ayyuby Schools",
            "credit": "Created by Mr. Ady Firman",
        },
    )
