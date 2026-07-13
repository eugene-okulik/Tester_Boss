import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step("Get object by ID")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}", headers=self.headers)
        if self.response.status_code == 200:
            self.json_response = self.response.json()
        return self.response
