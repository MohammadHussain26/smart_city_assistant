from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import generate_response

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
async def ask_city_assistant(request: Request, prompt: str = Form(...)):
    reply = generate_response(f"As a smart city assistant, answer: {prompt}")
    return templates.TemplateResponse("index.html", {"request": request, "response": reply})
