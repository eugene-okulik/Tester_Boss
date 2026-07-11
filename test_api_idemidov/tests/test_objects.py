import pytest
import allure


@allure.feature("API Testing")
@allure.story("Create Object")
@pytest.mark.parametrize(
    "name, job",
    [
        ("IvanTest1", "QA"),
        ("IvanTest2", "Developer"),
        ("IvanTest3", "Tester"),
    ],
)
def test_create_object(create_endpoint, name, job):
    """Тест создания объекта с параметризацией"""
    payload = {"name": name, "data": {"job": job}}

    create_endpoint.create_new_object(payload)
    create_endpoint.check_that_status_is_200()
    create_endpoint.check_response_name_is_correct(name)


@allure.feature("Important Features")
@allure.story("Update Object")
@allure.title("Full update via PUT")
@pytest.mark.critical
def test_put_object(update_endpoint, created_object_id):
    """Полное обновление объекта"""
    payload = {"name": "IvanPut", "data": {"job": "updated_status"}}

    update_endpoint.make_full_changes(created_object_id, payload)
    update_endpoint.check_that_status_is_200()
    update_endpoint.check_response_name_is_correct("IvanPut")


@allure.feature("Important Features")
@allure.story("Partial Update")
@allure.title("Partial update via PATCH")
@pytest.mark.medium
def test_patch_object(update_endpoint, created_object_id):
    """Частичное обновление объекта"""
    payload = {"name": "IvanPatch"}

    update_endpoint.make_partial_changes(created_object_id, payload)
    update_endpoint.check_that_status_is_200()
    update_endpoint.check_response_name_is_correct("IvanPatch")


@allure.feature("Basic Operations")
@allure.story("Get Object")
@allure.title("Get object by ID")
def test_get_object(get_delete_endpoint, created_object_id):
    """Получение объекта по ID"""
    get_delete_endpoint.get_object_by_id(created_object_id)
    get_delete_endpoint.check_that_status_is_200()
    get_delete_endpoint.check_response_id_is_correct(created_object_id)


@allure.feature("Basic Operations")
@allure.story("Delete Object")
@allure.title("Delete object and verify absence")
def test_delete_object(get_delete_endpoint, created_object_id):
    """Удаление объекта и проверка отсутствия"""
    # Удаляем
    get_delete_endpoint.delete_object_by_id(created_object_id)
    get_delete_endpoint.check_that_status_is_200()

    # Проверяем, что удален
    get_delete_endpoint.get_object_by_id(created_object_id)
    get_delete_endpoint.check_that_status_is_404()
