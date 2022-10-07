# Std
import os

# 3rd party
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

# Local
from . import base_endpoints
from .records import endpoints as record_endpoints
from .notes import endpoints as note_endpoints



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # ["https://localhost", "http://localhost:8080"]
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)



# App endpoints
app.include_router(base_endpoints.router)
app.include_router(record_endpoints.router, prefix="/records")
app.include_router(note_endpoints.router, prefix="/notes")