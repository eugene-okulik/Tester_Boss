import requests
import pytest

URL = "http://objapi.course.qa-practice.com/object"


# 1. Фикстуры для setup/teardown
@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def test_setup_teardown():
    print("\nbefore test")
    yield
    print("after test")


# 2. Фикстура для независимости тестов (создает и удаляет объект)
@pytest.fixture
def create_and_delete_object():
    """Создает объект перед тестом и удаляет после"""
    data = {"name": "TempObject", "data": {"job": "temp"}}
    resp = requests.post(URL, json=data)
    obj_id = resp.json()["id"]
    yield obj_id
    # Удаляем объект после теста
    requests.delete(f"{URL}/{obj_id}")


# 3. Тесты


@pytest.mark.parametrize(
    "name, job",
    [
        ("IvanTest1", "QA"),
        ("IvanTest2", "Developer"),
        ("IvanTest3", "Tester"),
    ],
)
def test_create(name, job):
    data = {"name": name, "data": {"job": job}}
    resp = requests.post(URL, json=data)
    assert resp.status_code == 200 or resp.status_code == 201
    assert resp.json()["name"] == name
    # Удаляем созданный объект, чтобы не мусорить
    requests.delete(f"{URL}/{resp.json()['id']}")


@pytest.mark.critical
def test_put(create_and_delete_object):
    obj_id = create_and_delete_object
    data = {"name": "IvanPut", "data": {"status": "updated"}}
    resp = requests.put(f"{URL}/{obj_id}", json=data)
    assert resp.status_code == 200
    assert resp.json()["name"] == "IvanPut"


@pytest.mark.medium
def test_patch(create_and_delete_object):
    obj_id = create_and_delete_object
    data = {"name": "IvanPatch"}
    resp = requests.patch(f"{URL}/{obj_id}", json=data)
    assert resp.status_code == 200
    assert resp.json()["name"] == "IvanPatch"


def test_get(create_and_delete_object):
    obj_id = create_and_delete_object
    resp = requests.get(f"{URL}/{obj_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == obj_id


def test_delete(create_and_delete_object):
    obj_id = create_and_delete_object

    # Удаляем объект
    delete_resp = requests.delete(f"{URL}/{obj_id}")
    assert delete_resp.status_code == 200

    # Проверяем, что он действительно удален (404)
    check_resp = requests.get(f"{URL}/{obj_id}")
    assert check_resp.status_code == 404
