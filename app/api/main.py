from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI BI Copilot running"}
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")