import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject


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
def get_endpoint():
    return GetObject()


@pytest.fixture
def delete_endpoint():
    return DeleteObject()


@pytest.fixture
def created_object_id(create_endpoint, delete_endpoint):
    """Фикстура для обеспечения независимости тестов."""
    payload = {"name": "TempObject", "data": {"job": "temp"}}
    create_endpoint.create_new_object(payload)
    create_endpoint.check_that_status_is_200()

    yield create_endpoint.object_id

    # Teardown: используем готовую фикстуру delete_endpoint
    # вместо ручного создания экземпляра класса
    delete_endpoint.delete_object_by_id(create_endpoint.object_id)
