import allure


@allure.feature("Main page")
def test_main_title(main_page):
    main_page.open()
    main_page.check_logo_is("Categories")
