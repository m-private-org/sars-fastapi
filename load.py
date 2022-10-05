import csv
import datetime

from app.records import models as records_models
from app.db.database import SessionLocal, engine

db = SessionLocal()

records_models.Base.metadata.create_all(bind=engine)

with open("sars_2003_complete_dataset_clean.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = records_models.Record(
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            country=row["country"],
            cases=row["cases"],
            deaths=row["deaths"],
            recoveries=row["recoveries"],
        )
        db.add(db_record)

    db.commit()

db.close()
