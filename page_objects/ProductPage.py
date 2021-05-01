from .BasePage import BasePage
import allure

URL = "https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49"


class ProductPage(BasePage):
    CURRENT_TITLE_ITEM = {'XPATH': '//div[@class="col-sm-4"]/h1'}
    TITLE_MAIN_PIC = {'XPATH': '//a[@class="thumbnail"]'}
    ADD_TO_CARD_BUTTON = {'id': 'button-cart'}
    ACTIVE_TAB_DESCRIPTION = {'id': 'tab-description'}
    INPUT_QUANTITY = {'XPATH': '//div[@class="form-group"]/input[1]'}
    HIDDEN = {'XPATH': '//div[@class="form-group"]/input[2]'}

    @allure.step(f"Open url: {URL}")
    def open(self):
        self.driver.get(URL)
        self.logger.info("Opening url:{}".format(URL))

    @allure.step("Get title current item")
    def get_title_current_item(self):
        element = self._find_element(self.CURRENT_TITLE_ITEM)
        self.logger.info("Get title current item")
        return element.text

    @allure.step("Get title of main pic")
    def get_title_main_pic(self):
        element = self._find_element(self.TITLE_MAIN_PIC)
        self.logger.info("Get title of main pic")
        return element.get_attribute("title")

    @allure.step("Get right panel title")
    def get_right_panel_title(self):
        element = self._find_element(self.CURRENT_TITLE_ITEM)
        self.logger.info("Get right panel title")
        return element.text

    @allure.step("Get text on 'add to card' button")
    def get_add_to_card_button_text(self):
        element = self._find_element(self.ADD_TO_CARD_BUTTON)
        self.logger.info("Get text on 'add to card' button")
        return element.text

    @allure.step("Show active tab description")
    def show_active_tab_description(self):
        element = self._find_element(self.ACTIVE_TAB_DESCRIPTION)
        self.logger.info("Show active tab description")
        return element.is_displayed()

    @allure.step("Get attribute 'name' on input_quantity field")
    def get_name_attribute_input_quantity(self):
        element = self._find_element(self.INPUT_QUANTITY)
        self.logger.info("Get attribute 'name' on input_quantity field")
        return element.get_attribute('name')
