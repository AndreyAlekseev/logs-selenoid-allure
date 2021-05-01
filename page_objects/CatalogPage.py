from .BasePage import BasePage
import allure

URL = "https://demo.opencart.com/index.php?route=product/category&path=20"


class CatalogPage(BasePage):
    SORT_BY_BUTTON = {'XPATH': '//select[@id="input-sort"]/option[1]'}
    SHOW_BY_BUTTON = {'XPATH': '//select[@id="input-limit"]/option[1]'}
    SYMBOL_CURRENT_CURRENCY = {'css': '#top .btn-link strong'}
    BREAD_CRUMBS_HOME_LINK = {'XPATH': '//ul[@class="breadcrumb"]/li[1]/a'}
    CONTENT_TITLE = {'XPATH': '//div[@id="content"]/h2'}
    BREAD_CRUMBS_CURRENT_LINK = {'XPATH': '//ul[@class="breadcrumb"]/li[2]/a'}

    @allure.step(f"Open url: {URL}")
    def open(self):
        self.driver.get(URL)
        self.logger.info("Opening url:{}".format(URL))

    @allure.step("get value of Sort By menu")
    def get_sort_by_value(self):
        element = self._find_element(self.SORT_BY_BUTTON)
        self.logger.info("get value of Sort By menu")
        return element.text

    @allure.step("get value of By count")
    def get_show_by_count(self):
        element = self._find_element(self.SHOW_BY_BUTTON)
        self.logger.info("get value of By count")
        return int(element.text)

    @allure.step("Show symbol current currency")
    def get_symbol_currency(self):
        element = self._find_element(self.SYMBOL_CURRENT_CURRENCY)
        self.logger.info("Show symbol current currency")
        return element.text

    @allure.step("Get home link of bread crumbs")
    def get_home_link_breadcrumbs(self):
        element = self._find_element(self.BREAD_CRUMBS_HOME_LINK)
        self.logger.info("Get home link of bread crumbs")
        return element.get_attribute("href")

    @allure.step("Get content title")
    def get_content_title(self):
        element = self._find_element(self.CONTENT_TITLE)
        self.logger.info("get content title")
        return element.text

    @allure.step("Get current link of bread crumbs")
    def get_current_breadcrumb_name(self):
        element = self._find_element(self.BREAD_CRUMBS_CURRENT_LINK)
        self.logger.info("get current link of bread crumbs")
        return element.text
