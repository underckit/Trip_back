import datetime

from sqlalchemy.orm import Session
import exception
import models
import schemas
from models import Executor, BusinessTrip, Expenses, TripExpenses
from schemas import ExpensesCreate, ExecutorCreate, BusinessTripCreate, TripExpensesCreate, Money
from collections import Counter


def create_executor(db: Session, executor: ExecutorCreate):
    _executor = Executor(full_name=executor.fullName, position=executor.position)
    db.add(_executor)
    db.commit()
    db.refresh(_executor)
    return _executor


def get_executors(db: Session):
    executors = db.query(models.Executor).all()
    exects = []
    for executor in executors:
        person = schemas.Executor(id=executor.id, fullName=executor.full_name, position=executor.position)
        exects.append(person)
    return exects


def create_trip(db: Session, trip: BusinessTripCreate):
    _trip = BusinessTrip(id_executor=trip.id_executor,
                         departure_point=trip.departure_point,
                         arrival_point=trip.arrival_point,
                         start_date=trip.start_date, end_date=trip.end_date)

    executor = db.query(models.Executor).filter(models.Executor.id == trip.id_executor).first()
    exception.NotFound(executor)
    db.add(_trip)
    db.commit()
    db.refresh(_trip)
    return _trip


def get_trips(db: Session):
    trips = db.query(models.BusinessTrip).all()
    return trips


def create_expense(db: Session, expense: ExpensesCreate):
    _expense = Expenses(type=expense.type, cost=expense.cost)
    db.add(_expense)
    db.commit()
    db.refresh(_expense)
    return _expense


def create_trip_expenses(db: Session, expenses: TripExpensesCreate):
    _expenses = TripExpenses(id_trip=expenses.id_trip, id_expenses=expenses.id_expenses)
    trip = db.query(models.BusinessTrip).filter(models.BusinessTrip.id == expenses.id_trip).first()
    exception.NotFound(trip)
    expense = db.query(models.Expenses).filter(models.Expenses.id == expenses.id_expenses).first()
    exception.NotFound(expense)
    db.add(_expenses)
    db.commit()
    db.refresh(_expenses)
    return _expenses


def get_all_info_trips(db: Session):
    trips = db.query(models.BusinessTrip).all()
    executors = db.query(models.Executor).all()
    expenses = db.query(models.Expenses).all()
    expenses_to_trip = db.query(models.TripExpenses).all()

    res = []

    for trip in trips:
        arr_exp = []
        for expense_to_tr in expenses_to_trip:
            if (trip.id == expense_to_tr.id_trip):
                for one_exp in expenses:
                    if (expense_to_tr.id_expenses == one_exp.id):
                        expense = schemas.Expenses(id=one_exp.id,
                                                   type=one_exp.type,
                                                   cost=one_exp.cost)
                        arr_exp.append(expense)

        for executor in executors:
            if (trip.id_executor == executor.id):
                executor_name = executor.full_name
                id_executor = executor.id
                executor_position = executor.position

        _trip = schemas.FullTripInfo(
            id=trip.id,
            executor_name=executor_name,
            id_executor=id_executor,
            executor_position=executor_position,
            departure_point=trip.departure_point,
            arrival_point=trip.arrival_point,
            start_date=trip.start_date,
            end_date=trip.end_date,
            expenses=arr_exp
        )
        res.append(_trip)
    return res


def get_old_trips(db: Session):
    now = datetime.date.today()
    trips = db.query(models.BusinessTrip).filter(models.BusinessTrip.end_date < now).all()
    executors = db.query(models.Executor).all()
    expenses = db.query(models.Expenses).all()
    expenses_to_trip = db.query(models.TripExpenses).all()

    res = []

    for trip in trips:
        arr_exp = []
        for expense_to_tr in expenses_to_trip:
            if (trip.id == expense_to_tr.id_trip):
                for one_exp in expenses:
                    if (expense_to_tr.id_expenses == one_exp.id):
                        expense = schemas.Expenses(id=one_exp.id,
                                                   type=one_exp.type,
                                                   cost=one_exp.cost)
                        arr_exp.append(expense)

        for executor in executors:
            if (trip.id_executor == executor.id):
                executor_name = executor.full_name
                id_executor = executor.id
                executor_position = executor.position

        _trip = schemas.FullTripInfo(
            id=trip.id,
            executor_name=executor_name,
            id_executor=id_executor,
            executor_position=executor_position,
            departure_point=trip.departure_point,
            arrival_point=trip.arrival_point,
            start_date=trip.start_date,
            end_date=trip.end_date,
            expenses=arr_exp
        )
        res.append(_trip)
    return res


def get_current_trips(db: Session):
    now = datetime.date.today()
    trips = db.query(models.BusinessTrip).filter(models.BusinessTrip.end_date >= now).all()
    executors = db.query(models.Executor).all()
    expenses = db.query(models.Expenses).all()
    expenses_to_trip = db.query(models.TripExpenses).all()
    res = []
    for trip in trips:
        arr_exp = []
        for expense_to_tr in expenses_to_trip:
            if (trip.id == expense_to_tr.id_trip):
                for one_exp in expenses:
                    if (expense_to_tr.id_expenses == one_exp.id):
                        expense = schemas.Expenses(id=one_exp.id,
                                                   type=one_exp.type,
                                                   cost=one_exp.cost)
                        arr_exp.append(expense)

        for executor in executors:
            if (trip.id_executor == executor.id):
                executor_name = executor.full_name
                id_executor = executor.id
                executor_position = executor.position

        _trip = schemas.FullTripInfo(
            id=trip.id,
            executor_name=executor_name,
            id_executor=id_executor,
            executor_position=executor_position,
            departure_point=trip.departure_point,
            arrival_point=trip.arrival_point,
            start_date=trip.start_date,
            end_date=trip.end_date,
            expenses=arr_exp
        )
        res.append(_trip)
    return res

#сколько  всего потрачено на командирои
def get_all_money_for_trips(db:Session):
    now = datetime.date.today()
    trips = db.query(models.BusinessTrip).filter(models.BusinessTrip.start_date <= now).all()
    expenses = db.query(models.Expenses).all()
    expenses_to_trip = db.query(models.TripExpenses).all()
    summary = 0
    for trip in trips:
        for expense_to_tr in expenses_to_trip:
            if trip.id == expense_to_tr.id_trip:
                for one_exp in expenses:
                    if expense_to_tr.id_expenses == one_exp.id:
                        summary += one_exp.cost

    sum = schemas.Money(money=summary)
    return sum

def count_repeats(lst):
    """
    Возвращает словарь, в котором каждому элементу списка lst соответствует
    количество его повторений.
    """
    repeats = {}
    for item in lst:
        if item in repeats:
            repeats[item] += 1
        else:
            repeats[item] = 1
    return repeats

# куда чаще всего гоняли в командировки
def get_top_cities(db:Session):

    trips = db.query(models.BusinessTrip).\
        order_by(models.BusinessTrip.arrival_point.desc()).all()
    arr = []
    for trip in trips:
        arr.append(trip.arrival_point)
    dict = count_repeats(arr)
    return dict
"""select arrival_point,count(id) as city_count from business_trip 
group by arrival_point order by city_count desc;"""

