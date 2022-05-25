from sqlalchemy import Column, Integer, Float, Date
from database import Base

class Weight(Base):
    __tablename__ = "weight"
    id = Column(Integer, primary_key=True)
    date = Column(Date())
    weight = Column(Float())