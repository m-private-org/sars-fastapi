import os

from fastapi import APIRouter
from starlette.responses import RedirectResponse


router = APIRouter()

@router.get("/")
def main():
    return RedirectResponse(url="/docs/")

@router.get("/ping")
def pong():
    return {"ping": "pong!"}

@router.get("/health/")
def health():
    return {
        "env_version": os.getenv("env_version")
    }