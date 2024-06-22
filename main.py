from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Stel de statische bestanden directory in
app.mount("/Frontend", StaticFiles(directory="Frontend"), name="frontend")

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Lees de inhoud van het HTML-bestand
    html_content = Path("Frontend/index.html").read_text()
    return html_content

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"message": f"Hello, {name}!"}
