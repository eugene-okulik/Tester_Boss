import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step("Delete object by ID")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}", headers=self.headers)
        return self.response
