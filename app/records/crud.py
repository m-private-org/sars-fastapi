from sqlalchemy.orm import Session
from . import models, schemas


def get_record(db: Session, id: int):
    return db.query(models.Record).get(models.Record.id == id).first()


def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(record)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

