import allure
from page_objects import LoginPage


def test_success_login(browser):
    LoginPage(browser).go_site()
    LoginPage(browser).login()
    LoginPage(browser).switch_to_frame()
    with allure.step("Сравниваю текст подписи"):
        assert LoginPage(browser).sign() == LoginPage(browser).SIGN


def test_incorrect_login(browser):
    LoginPage(browser).go_site()
    LoginPage(browser).login_incorrect_param()
    with allure.step("Сравниваю текст ошибки"):
        assert LoginPage(browser).incorrect_parameter() == LoginPage(browser).INCORRECT_PARAMETER


def test_forgot_password(browser):
    LoginPage(browser).go_site()
    LoginPage(browser).forgot_password()
    with allure.step("Сравниваю текст уведомления"):
        assert LoginPage(browser).incorrect_parameter() == LoginPage(browser).FORGOT_PASSWORD_TEXT


def test_new_user(browser):
    LoginPage(browser).go_site()
    LoginPage(browser).new_user()
    with allure.step("Сравниваю текст кнопки создания юзера"):
        assert LoginPage(browser).button() == LoginPage(browser).NEW_USER_TEXT
