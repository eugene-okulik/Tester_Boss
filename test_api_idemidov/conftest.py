import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.get_delete_object import GetDeleteObject


@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    print("\nStart testing session")
    yield
    print("\nTesting session completed")


@pytest.fixture(autouse=True)
def test_setup_teardown():
    print("\nbefore test")
    yield
    print("after test")


@pytest.fixture
def create_endpoint():
    return CreateObject()


@pytest.fixture
def update_endpoint():
    return UpdateObject()


@pytest.fixture
def get_delete_endpoint():
    return GetDeleteObject()


@pytest.fixture
def created_object_id(create_endpoint):
    """Фикстура для обеспечения независимости тестов.
    Создает объект перед тестом и удаляет после."""
    payload = {"name": "TempObject", "data": {"job": "temp"}}
    create_endpoint.create_new_object(payload)
    create_endpoint.check_that_status_is_200()

    yield create_endpoint.object_id

    # Teardown: удаление объекта после теста
    get_delete_ep = GetDeleteObject()
    get_delete_ep.delete_object_by_id(create_endpoint.object_id)
