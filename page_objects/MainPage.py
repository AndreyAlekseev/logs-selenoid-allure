from .BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

URL = "https://demo.opencart.com"


class MainPage(BasePage):
    LINK_IN_FOOTER_ON_LABEL = {'XPATH': '//div[@class="container"]/p/a'}
    CART_BUTTON = {'id': 'cart'}
    ELEMENT_ON_FEATURE_ROW = (By.XPATH, "//div[@class='product-thumb transition']")
    ACCOUNT_DROPDOWN_BUTTON = {'XPATH': '//li[@class="dropdown"]/a[@title="My Account"]'}
    LOGO = {'id': 'logo'}

    @allure.step(f"Open url: {URL}")
    def open(self):
        self.driver.get(URL)
        self.logger.info("Opening url:{}".format(URL))

    @allure.step("Get link text on label in footer")
    def get_link_text_on_label(self):
        element = self._find_element(self.LINK_IN_FOOTER_ON_LABEL)
        self.logger.info("Get link text on label in footer")
        return element.text

    @allure.step("Show cart button")
    def show_cart_button(self):
        element = self._find_element(self.CART_BUTTON)
        self.logger.info("Show cart button")
        return element.is_displayed()

    @allure.step("Get count of displayed featured elements")
    def count_display_featured_elements(self):
        count = self._find_elements(self.ELEMENT_ON_FEATURE_ROW)
        self.logger.info("Get count of displayed featured elements")
        return len(count)

    @allure.step("Get title account button dropdown")
    def get_title_account_dropdown(self):
        element = self._find_element(self.ACCOUNT_DROPDOWN_BUTTON)
        self.logger.info("Get title account button dropdown")
        return element.get_attribute("title")

    @allure.step("Get text on logo")
    def get_text_logo(self):
        element = self._find_element(self.LOGO)
        self.logger.info("Get text on logo")
        return element.text
