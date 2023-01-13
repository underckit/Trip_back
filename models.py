import datetime
import uuid
from uuid import UUID

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from config import Base




class Executor(Base):
    __tablename__ = "executor"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    position = Column(String)

class BusinessTrip(Base):
    __tablename__ = "business_trip"

    id = Column(Integer, primary_key=True)
    id_executor = Column(Integer, ForeignKey("executor.id"))
    departure_point = Column(String)
    arrival_point = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)


class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    cost = Column(Integer)

class TripExpenses(Base):
    __tablename__ = "trip_expenses"

    id = Column(Integer, primary_key=True)
    id_trip = Column(Integer, ForeignKey("business_trip.id"))
    id_expenses = Column(Integer, ForeignKey("expenses.id"))