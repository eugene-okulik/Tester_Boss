import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step("Create a new object")
    def create_new_object(self, payload):
        # Твой API требует вложенную структуру data для job
        self.response = requests.post(self.url, json=payload, headers=self.headers)

        if self.response.status_code in [200, 201]:
            self.json_response = self.response.json()
            self.object_id = self.json_response.get("id")
        else:
            self.json_response = {}

        return self.response
