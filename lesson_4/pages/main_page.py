from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    BUTTON_NOT_NOW = (By.XPATH, "//button[text() = 'Not Now' or text() = 'Не сейчас']")
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder='Search' or @placeholder='Поиск']")

    def _verify_page(self):
        self.on_this_page(self.FIELD_SEARCH)

    def click_not_now_button(self):
        self.click_if_exists(self.BUTTON_NOT_NOW)

    def typein_search_field(self, keyword_for_search):
        self.type_in(self.FIELD_SEARCH, keyword_for_search)

    def click_search_result(self, keyword):
        search_result = (By.XPATH, "//span[text()='{}']".format(keyword))
        self.click_on(search_result)