from .BasePage import BasePage
import allure

URL = "https://demo.opencart.com/admin/"


class AdminPage(BasePage):
    INPUT_USERNAME = {'id': 'input-username'}
    INPUT_PASSWORD = {'id': 'input-password'}
    SUBMIT_BUTTON = {'XPATH': '//button'}
    MAP_TITLE = {'class': 'panel-title'}
    LOGO_ON_START_PAGE = {'css': '.navbar-brand > img'}
    PANEL_TITLE = {'class': 'panel-title'}
    FORGOTTEN_PASSWORD_BUTTON = {'XPATH': "//span[@class='help-block']"}
    ERROR_MESSAGE = {'XPATH': "//div[@class='panel-body']/div"}

    @allure.step(f"Open url: {URL}")
    def open(self):
        self.driver.get(URL)
        self.logger.info("Opening url:{}".format(URL))

    @allure.step("Authorizing with Login and Password")
    def login_user(self, login, password):
        self.logger.info("Login into\n" + "username: {}\n".format(login) + "password: {}".format(password))
        self._input(self.INPUT_USERNAME, login)
        self._input(self.INPUT_PASSWORD, password)
        self._click(self.SUBMIT_BUTTON)

    @allure.step("Get title map on admin page")
    def get_title_map(self):
        element = self._get_element_text(self.MAP_TITLE)
        self.logger.info("Show text property of element ")
        return element

    @allure.step("Get logo attribute")
    def get_logo_attribute(self, value):
        element = self._find_element(self.LOGO_ON_START_PAGE)
        self.logger.info("Show attribute of element")
        return element.get_attribute(value)

    @allure.step("Get title login form")
    def get_title_login_form(self):
        element = self._get_element_text(self.PANEL_TITLE)
        self.logger.info("Show title login form")
        return element

    @allure.step("Checking is activities submit button")
    def submit_button_is_active(self):
        element = self._find_element(self.SUBMIT_BUTTON)
        self.logger.info("Activate submit button")
        return element.is_enabled()

    @allure.step("Contain the text on the button 'forgotten password button'")
    def get_forgotten_password_button_text(self):
        element = self._get_element_text(self.FORGOTTEN_PASSWORD_BUTTON)
        self.logger.info("Show text on forgotten password button")
        return element

    @allure.step("Show username field")
    def username_field_is_displayed(self):
        element = self._find_element(self.INPUT_USERNAME)
        self.logger.info("Show username field")
        return element.is_displayed()

    @allure.step("Show error message")
    def error_message_is_displayed(self):
        element = self._find_element(self.ERROR_MESSAGE)
        self.logger.info("Show error message")
        return element.is_displayed()
