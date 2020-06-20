import allure
from page_objects import MainPage
from page_objects import LoginPage


def test_navigate_requirements(browser):
    """проверка перехода в требования"""
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).requirements_button()
    MainPage(browser).switch_to_mainframe()
    MainPage(browser).switch_to_treeframe()
    with allure.step("Сравниваю название раздела"):
        assert MainPage(browser).requirements_title() == MainPage(browser).REQUIREMENTS_TEXT


def test_navigate_test_specifications(browser):
    """проверка перехода в спецификации"""
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).specification_button()
    MainPage(browser).switch_to_mainframe()
    MainPage(browser).switch_to_treeframe()
    with allure.step("Сравниваю название раздела"):
        assert MainPage(browser).specification_title() == MainPage(browser).TEST_SPECIFICATION_TEXT


def test_navigate_test_execution(browser):
    """проверка перехода в выполняемые тесты"""
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).test_execution_button()
    MainPage(browser).switch_to_mainframe()
    MainPage(browser).switch_to_treeframe()
    with allure.step("Сравниваю название раздела"):
        assert MainPage(browser).test_execution_title() == MainPage(browser).EXECUTE_TEST_TEXT


def test_navigate_plugins(browser):
    """проверка перехода в плагины """
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).plugins_button()
    MainPage(browser).switch_to_mainframe()
    MainPage(browser).tab_title()
    with allure.step("Сравниваю название раздела"):
        assert MainPage(browser).tab_title() == MainPage(browser).PLUGINS_TEXT


def test_events(browser):
    """проверка перехода в эвенты"""
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).events_button()
    MainPage(browser).switch_to_mainframe()
    MainPage(browser).tab_title()
    with allure.step("Сравниваю название раздела"):
        assert MainPage(browser).tab_title() == MainPage(browser).EVENTS_TEXT


def test_logout(browser):
    """проверка разлогина"""
    MainPage(browser).go_site()
    LoginPage(browser).login()
    MainPage(browser).logout_button()
    with allure.step("Сравниваю название кнопки"):
        assert LoginPage(browser).button() == LoginPage(browser).LOGIN
