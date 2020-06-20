import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost/testlink/login.php"

    def go_site(self):
        with allure.step(f"Перехожу на адрес {self.base_url}"):
            return self.driver.get(self.base_url)

    MAIN_FRAME = "mainframe"
    PAGE = "h6"
    TEXT_ERROR = "user__feedback"
    FORGOT_PASSWORD = "Забыли пароль?"
    ATTRIBUTE = "value"
    NEW_USER = "Новый пользователь?"
    SIGN = "Powered by TestLink 1.9.19 (Metonic cycle)"
    INCORRECT_PARAMETER = "Попробуйте снова! Вы ввели неверное имя или пароль!"
    FORGOT_PASSWORD_TEXT = "Введите Ваш логин, и Testlink отправит новый пароль на указанный Вами при регистрации email."
    NEW_USER_TEXT = "Добавить данные пользователя"
    SUBMIT = "input[type=submit]"
    LOGIN = "Войти"

    def login(self):
        with allure.step("Логин на главную страницу"):
            self.driver.find_element_by_id("tl_login").send_keys("admin")
            self.driver.find_element_by_id("tl_password").send_keys("123456")
            self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def switch_to_frame(self):
        with allure.step("Переключение на главный фрейм"):
            self.driver.switch_to.frame(self.MAIN_FRAME)

    def sign(self):
        with allure.step("Получаю текст подписи"):
            nam = self.driver.find_element_by_tag_name(self.PAGE).text
            return nam

    def login_incorrect_param(self):
        with allure.step("Ввод некорректных данных для логина"):
            self.driver.find_element_by_id("tl_login").send_keys("adminn")
            self.driver.find_element_by_id("tl_password").send_keys("123456")
            self.driver.find_element_by_css_selector("input[type=submit]").click()

    def incorrect_parameter(self):
        with allure.step("Получаю ошибку при вводе неправильных параметров"):
            err = self.driver.find_element_by_class_name(self.TEXT_ERROR).text
            return err

    def forgot_password(self):
        with allure.step("Нажимаю кнопку восстановления пароля"):
            self.driver.find_element_by_link_text(self.FORGOT_PASSWORD).click()

    def new_user(self):
        with allure.step("Нажимаю кнопку создания нового юзера"):
            self.driver.find_element_by_link_text(self.NEW_USER).click()

    def button(self):
        button_text = self.driver.find_element_by_css_selector(self.SUBMIT).get_attribute(self.ATTRIBUTE)
        return button_text
