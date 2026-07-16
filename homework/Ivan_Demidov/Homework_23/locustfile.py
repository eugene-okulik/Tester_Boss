from locust import task, HttpUser
import random


class ObjectUser(HttpUser):
    object_id = None

    def on_start(self):
        response = self.client.post(
            "/object",
            json={
                "name": f"Object {random.randint(1, 1000)}",
                "data": {"key": "value"},
            },
        )
        if response.status_code in [200, 201]:
            self.object_id = response.json().get("id")

    @task(3)
    def get_one_object(self):
        if self.object_id:
            self.client.get(f"/object/{self.object_id}")

    @task(2)
    def update_object_put(self):
        if self.object_id:
            self.client.put(
                f"/object/{self.object_id}",
                json={
                    "name": f"Updated {random.randint(1, 1000)}",
                    "data": {"status": "updated"},
                },
            )

    @task(2)
    def update_object_patch(self):
        if self.object_id:
            self.client.patch(
                f"/object/{self.object_id}",
                json={"name": f"Patched {random.randint(1, 1000)}"},
            )

    @task(1)
    def delete_object(self):
        if self.object_id:
            self.client.delete(f"/object/{self.object_id}")
            self.object_id = None
