import allure


@allure.feature("Login")
def test_incorrect_login(customer_login):
    customer_login.open()
    customer_login.enter_email("fds@sfsdf.com")
    customer_login.enter_password("dfsfsdfdsfdf")
    customer_login.click_submit_button()
    customer_login.check_error_alert("Wrong login/password")
