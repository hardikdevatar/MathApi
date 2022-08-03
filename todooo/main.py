from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import statistics
import numpy as np


# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "Math Api"

@app.post("/min",status_code=status.HTTP_200_OK)
async def minCall(request: schemas.mathCreate, session: Session = Depends(get_session)):
    return min(request.listOfNumbers)

@app.post("/max",status_code=status.HTTP_200_OK)
def maxCall(request: schemas.mathCreate, session: Session = Depends(get_session)):
    return max(request.listOfNumbers)

@app.post("/avg",status_code=status.HTTP_200_OK)
def avgCall(listOfNumbers: list, session: Session = Depends(get_session)):
    return sum(listOfNumbers) / len(listOfNumbers)

@app.post("/median",status_code=status.HTTP_200_OK)
def medianCall(listOfNumbers: list, session: Session = Depends(get_session)):
    return statistics.median(listOfNumbers)

@app.post("/percentile",status_code=status.HTTP_200_OK)
def percentileCall(request: schemas.mathCreate, session: Session = Depends(get_session)):
    return np.percentile(request.listOfNumbers, request.quantifier)
