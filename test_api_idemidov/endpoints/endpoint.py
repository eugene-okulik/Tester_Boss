import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json_response = None
    headers = {"Content-type": "application/json; charset=UTF-8"}

    @allure.step("Check that status code is 200")
    def check_that_status_is_200(self):
        assert (
            self.response.status_code == 200
        ), f"Expected 200, got {self.response.status_code}. Response: {self.response.text}"

    @allure.step("Check that name in response matches expected")
    def check_response_name_is_correct(self, expected_name):
        actual_name = self.json_response.get("name")
        assert (
            actual_name == expected_name
        ), f"Name mismatch. Expected: '{expected_name}', Got: '{actual_name}'"

    @allure.step("Check that object ID matches expected")
    def check_response_id_is_correct(self, expected_id):
        actual_id = self.json_response.get("id")
        assert (
            actual_id == expected_id
        ), f"ID mismatch. Expected: {expected_id}, Got: {actual_id}"

    @allure.step("Check that status code is 404")
    def check_that_status_is_404(self):
        assert (
            self.response.status_code == 404
        ), f"Expected 404, got {self.response.status_code}. Response: {self.response.text}"
