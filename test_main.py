from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_executors():
    response = client.get("/crud/get_executors/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "fullName": "Иванов Иван Иванович",
            "position": "Инженер",
            "id": 1
        },
        {
            "fullName": "Чернов Сергей Петрович",
            "position": "Инженер",
            "id": 2
        },
        {
            "fullName": "Крестов Александр Васильевич",
            "position": "Бухгалтер",
            "id": 3
        }
    ]


def test_create_trip():
    response = client.post(
        "/crud/create_business_trip/",
        json={"id_executor": 2,
              "departure_point": "Волгоград",
              "arrival_point": "Москва",
              "start_date": "2023-01-18",
              "end_date": "2023-01-19"},
    )
    assert response.status_code == 200


def test_get_trip_info():
    response = client.get("/crud/get_all_info_trips/")
    assert response.status_code == 200


def test_get_cities():
    response = client.get("/crud/get_top_cities/")
    assert response.status_code == 200


def test_get_money():
    response = client.get("crud/get_all_money_for_trips/")
    assert response.status_code == 200


def test_get_current_trip_info():
    response = client.get("/crud/get_current_trips/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 2,
            "executor_name": "Чернов Сергей Петрович",
            "id_executor": 2,
            "executor_position": "Инженер",
            "departure_point": "Волгоград",
            "arrival_point": "Астрахань",
            "start_date": "2023-01-11",
            "end_date": "2023-01-31",
            "expenses": [
                {
                    "type": "Питание",
                    "cost": 6000,
                    "id": 2
                },
                {
                    "type": "Непредвиденные расходы",
                    "cost": 2500,
                    "id": 3
                }
            ]
        }
    ]
