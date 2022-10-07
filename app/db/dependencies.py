
from sqlalchemy.orm import Session

from .database import SessionLocal, engine

# Create all tables
# TODO: find a better way to do this
from ..records import models as records_models
from ..notes import models as notes_models
records_models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()