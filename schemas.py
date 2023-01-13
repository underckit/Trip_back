import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel, Field


class ExecutorCreate(BaseModel):
    fullName: str
    position: str


class Executor(ExecutorCreate):
    id: int

    class Config:
        orm_mode = True


class BusinessTripCreate(BaseModel):
    id_executor: int
    departure_point: str
    arrival_point: str
    start_date: datetime.date
    end_date: datetime.date


class BusinessTrip(BusinessTripCreate):
    id: int

    class Config:
        orm_mode = True


class ExpensesCreate(BaseModel):
    type: str
    cost: int


class Expenses(ExpensesCreate):
    id: int

    class Config:
        orm_mode = True


class TripExpensesCreate(BaseModel):
    id_trip: int
    id_expenses: int


class TripExpenses(TripExpensesCreate):
    id: int

    class Config:
        orm_mode = True


class FullTripInfo(BaseModel):
    id: int
    executor_name: str
    id_executor: int
    executor_position: str
    departure_point: str
    arrival_point: str
    start_date: datetime.date
    end_date: datetime.date
    expenses: List[Expenses]


class Money(BaseModel):
    money: int
