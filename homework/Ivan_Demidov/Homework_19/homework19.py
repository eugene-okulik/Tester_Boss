import requests

URL = "http://objapi.course.qa-practice.com/object"


# 1. Создание (POST)
def test_create():
    data = {"name": "IvanTest", "data": {"job": "QA"}}
    resp = requests.post(URL, json=data)
    print(f"POST Status: {resp.status_code}")
    obj_id = resp.json()["id"]
    print(f"Created ID: {obj_id}")
    return obj_id


# 2. Изменение целиком (PUT)
def test_put(obj_id):
    data = {"name": "IvanPut", "data": {"status": "updated"}}
    resp = requests.put(f"{URL}/{obj_id}", json=data)
    print(f"PUT Status: {resp.status_code}")
    assert resp.json()["name"] == "IvanPut"


# 3. Частичное изменение (PATCH)
def test_patch(obj_id):
    data = {"name": "IvanPatch"}  # Меняем только имя
    resp = requests.patch(f"{URL}/{obj_id}", json=data)
    print(f"PATCH Status: {resp.status_code}")
    assert resp.json()["name"] == "IvanPatch"


# 4. Удаление (DELETE)
def test_delete(obj_id):
    resp = requests.delete(f"{URL}/{obj_id}")
    print(f"DELETE Status: {resp.status_code}")

    # Проверка, что удалился
    check = requests.get(f"{URL}/{obj_id}")
    print(f"Check Deleted Status: {check.status_code} (должно быть 404)")


if __name__ == "__main__":
    try:
        new_id = test_create()
        test_put(new_id)
        test_patch(new_id)
        test_delete(new_id)
        print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ")
    except Exception as e:
        print(f"\nОШИБКА: {e}")
