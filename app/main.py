# Std
import os

# 3rd party
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

# Local
from  .records import endpoints


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # ["https://localhost", "http://localhost:8080"]
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/ping/")
def ping():
    return 'pong'

@app.get("/health/")
def health():
    return {
        "env_version": os.getenv("env_version"),
        "m-private-mysql-root-pass": os.getenv("m-private-mysql-root-pass"),
    }

# App endpoints
app.include_router(endpoints.router, prefix="/records")