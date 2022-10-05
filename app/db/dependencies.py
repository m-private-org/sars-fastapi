
from sqlalchemy.orm import Session

from .database import SessionLocal, engine

from ..records import models as records_models


records_models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()