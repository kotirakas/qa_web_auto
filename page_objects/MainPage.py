import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/testlink/login.php"

    def go_site(self):
        with allure.step(f"Перехожу на адрес {self.base_url}"):
            return self.driver.get(self.base_url)

    MAIN_FRAME = "mainframe"
    TITLEBAR = "titlebar"
    TREEFRAME = "treeframe"
    REQUIREMENTS_BUTTON = "img[title='Requirements']"
    REQUIREMENTS_NAME = "#ext-gen11 h1.title"
    REQUIREMENTS_TEXT = "Navigator - Requirement Specifications"
    TEST_SPECIFICATION_BUTTON = "img[title='Test Specification']"
    TEST_SPECIFICATION_NAME = "#ext-gen12 h1.title"
    TEST_SPECIFICATION_TEXT = "Navigator - Test Specification"
    TEST_EXECUTION_BUTTON = "img[title='Test Execution']"
    EXECUTE_TEST_NAME = "#ext-gen12 h1.title"
    EXECUTE_TEST_TEXT = "Execute Tests"
    PLUGINS_BUTTON = "img[title='Plugins']"
    TAB_NAME = "h1"
    PLUGINS_TEXT = "Available Plugins"
    EVENTS_BUTTON = "img[title='Events']"
    EVENTS_NAME = "h1"
    EVENTS_TEXT = "Event viewer"
    LOGOUT_BUTTON = "img[title='Logout']"
    SUBMIT = "input[type=submit]"

    def switch_to_mainframe(self):
        with allure.step(f"перехожу на фрейм {self.MAIN_FRAME}"):
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.MAIN_FRAME)

    def switch_to_treeframe(self):
        with allure.step(f"перехожу на фрейм {self.TREEFRAME}"):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.frame_to_be_available_and_switch_to_it(self.TREEFRAME))

    def requirements_button(self):
        with allure.step("Нажимаю на кнопку Requirement"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.REQUIREMENTS_BUTTON).click()

    def requirements_title(self):
        with allure.step("Получаю название раздела"):
            title = self.driver.find_element_by_css_selector(self.REQUIREMENTS_NAME).text
            return title

    def specification_button(self):
        with allure.step("Нажимаю на кнопку Test specification"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.TEST_SPECIFICATION_BUTTON).click()

    def specification_title(self):
        with allure.step("Получаю название раздела"):
            title = self.driver.find_element_by_css_selector(self.TEST_SPECIFICATION_NAME).text
            return title

    def test_execution_button(self):
        with allure.step("Нажимаю на кнопку Test execution"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.TEST_EXECUTION_BUTTON).click()

    def test_execution_title(self):
        with allure.step("Получаю название раздела"):
            title = self.driver.find_element_by_css_selector(self.EXECUTE_TEST_NAME).text
            return title

    def plugins_button(self):
        with allure.step("Нажимаю на кнопку Plugins"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.PLUGINS_BUTTON).click()

    def events_button(self):
        with allure.step("Нажимаю на кнопку Events"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.EVENTS_BUTTON).click()

    def tab_title(self):
        with allure.step("Получаю название раздела"):
            wait = WebDriverWait(self.driver, 5)
            title = wait.until(EC.presence_of_element_located((By.TAG_NAME, self.TAB_NAME))).text
            return title

    def logout_button(self):
        with allure.step("Нажимаю на кнопку Logout"):
            self.driver.switch_to.frame('titlebar')
            self.driver.find_element_by_css_selector(self.LOGOUT_BUTTON).click()

    def login(self):
        with allure.step("Логин на главную страницу"):
            self.driver.find_element_by_id("tl_login").send_keys("admin")
            self.driver.find_element_by_id("tl_password").send_keys("123456")
            self.driver.find_element_by_css_selector(self.SUBMIT).click()
