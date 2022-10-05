from typing import List

from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends

from . import models, schemas
from ..db.dependencies import get_db


router = APIRouter()


# @router.get("/")
# async def index():
#     return {"message": "polls index"}


@router.get("/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records
