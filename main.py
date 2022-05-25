from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
import models
import schemas
import datetime
from database import engine, Base, SessionLocal

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def read_weight(session: Session = Depends(get_session)):

    weight_list = session.query(models.Weight).all()

    return weight_list


@app.post("/weight", status_code=status.HTTP_201_CREATED)
def create_weight(weight: schemas.WeightCreate, session: Session = Depends(get_session)):

    weightdb = models.Weight(weight=weight.weight, date=weight.date)

    session.add(weightdb)
    session.commit()
    session.refresh(weightdb)

    return weightdb