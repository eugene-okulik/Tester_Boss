import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step("Update an existing object via PUT")
    def make_full_changes(self, object_id, payload):
        self.response = requests.put(
            f"{self.url}/{object_id}", json=payload, headers=self.headers
        )
        self.json_response = self.response.json()
        return self.response

    @allure.step("Partially update an existing object via PATCH")
    def make_partial_changes(self, object_id, payload):
        self.response = requests.patch(
            f"{self.url}/{object_id}", json=payload, headers=self.headers
        )
        self.json_response = self.response.json()
        return self.response
