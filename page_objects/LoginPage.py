from .BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

URL = "https://demo.opencart.com/index.php?route=account/login"


class LoginPage(BasePage):
    LOGIN_INPUT = {'id': 'input-email'}
    LOGIN_PASSWORD = {'id': 'input-password'}
    RIGHT_MENU_ROWS = (By.XPATH, '//div[@class="list-group"]/a')
    LEFT_BLOCK_DESCRIPTION = (By.XPATH, '//div[@class="well"]/p/strong')
    TOP_NAVBAR = {'id': 'menu'}

    @allure.step(f"Open url: {URL}")
    def open(self):
        self.driver.get(URL)
        self.logger.info("Opening url:{}".format(URL))

    @allure.step("Get text placeholder username field")
    def get_placeholder_username(self):
        element = self._find_element(self.LOGIN_INPUT)
        self.logger.info("Get text placeholder username field")
        return element.get_attribute("placeholder")

    @allure.step("Get text placeholder password field")
    def get_placeholder_password(self):
        element = self._find_element(self.LOGIN_PASSWORD)
        self.logger.info("Get text placeholder password field")
        return element.get_attribute("placeholder")

    @allure.step("Get count rows of right menu")
    def get_count_rows_of_right_menu(self):
        count = self._find_elements(self.RIGHT_MENU_ROWS)
        self.logger.info("Get count rows of right menu")
        return len(count)

    @allure.step("Get subtitle text on left block description")
    def get_subtitle_text_on_description(self):
        element = self._find_elements(self.LEFT_BLOCK_DESCRIPTION)
        self.logger.info("Get subtitle text on left block description")
        return element[0].text

    @allure.step("Show top navbar")
    def show_top_navbar(self):
        element = self._find_element(self.TOP_NAVBAR)
        self.logger.info("Show top navbar")
        return element.is_displayed()
