from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from ..db.database import Base, engine


class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String(255), index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)
