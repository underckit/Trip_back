from typing import List

from fastapi import APIRouter, HTTPException, Path, Depends

import schemas
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import ExecutorCreate, BusinessTripCreate, ExpensesCreate, TripExpensesCreate, Executor
from methods import crud

router = APIRouter(
    prefix="/crud",
    tags=["crud"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create_executor')
def create_executor(executor: ExecutorCreate, db: Session = Depends(get_db)):
    return crud.create_executor(db, executor)


@router.get('/get_executors', response_model=List[schemas.Executor])
def get_executors(db: Session = Depends(get_db)):
    executors = crud.get_executors(db)
    return executors


@router.post('/create_business_trip')
def create_executor(trip: BusinessTripCreate, db: Session = Depends(get_db)):
    return crud.create_trip(db, trip)

@router.get('/get_business_trips', response_model=List[schemas.BusinessTrip])
def get_trips(db: Session = Depends(get_db)):
    trips = crud.get_trips(db)
    return trips


@router.post('/create_expense')
def create_executor(expense: ExpensesCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)


@router.post('/create_trip_expenses')
def create_trip_expenses(expenses: TripExpensesCreate, db: Session = Depends(get_db)):
    return crud.create_trip_expenses(db, expenses)


@router.get('/get_all_info_trips', response_model=List[schemas.FullTripInfo])
def get_all_info_trips(db: Session = Depends(get_db)):
    return crud.get_all_info_trips(db)

@router.get('/get_old_trips', response_model=List[schemas.FullTripInfo]) #завершенные командировки
def get_old_trips(db: Session = Depends(get_db)):
    return crud.get_old_trips(db)

@router.get('/get_current_trips', response_model=List[schemas.FullTripInfo]) #актуальные командировки
def get_current_trips(db: Session = Depends(get_db)):
    return crud.get_current_trips(db)

@router.get('/get_all_money_for_trips', response_model= schemas.Money) #бюджет за все время
def get_all_money_for_trips(db: Session = Depends(get_db)):
    return crud.get_all_money_for_trips(db)

@router.get('/get_top_cities', response_model= dict) #топ городов
def get_top_cities(db: Session = Depends(get_db)):
    return crud.get_top_cities(db)