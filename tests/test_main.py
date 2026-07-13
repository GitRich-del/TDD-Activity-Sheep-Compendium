import os
import sys

from fastapi.testclient import TestClient

# Add the project root to the path so test execution works reliably in class setups.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app  # noqa: E402


client = TestClient(app)


def test_get_sheep_by_id() -> None:
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "female",
    }


def test_add_sheep() -> None:
    sheep_data = {
        "id": 3,
        "name": "Mochi",
        "breed": "Babydoll Southdown",
        "sex": "female",
    }
    response = client.post("/sheep", json=sheep_data)
    assert response.status_code == 201
    assert response.json() == sheep_data


def test_update_sheep() -> None:
    updated_data = {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe",
    }
    response = client.put("/sheep/1", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data


def test_get_all_sheep() -> None:
    response = client.get("/sheep")
    assert response.status_code == 200
    sheep_list = response.json()
    assert isinstance(sheep_list, list)
    assert any(s["id"] == 1 for s in sheep_list)


def test_delete_sheep() -> None:
    response = client.delete("/sheep/2")
    assert response.status_code == 204

    get_deleted = client.get("/sheep/2")
    assert get_deleted.status_code == 404
