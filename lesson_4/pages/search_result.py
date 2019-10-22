from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResult(BasePage):
    BUTTON_FOLLOW = (By.XPATH, "//button[@type='button']")

    def _verify_page(self):
        self.on_this_page(self.BUTTON_FOLLOW)

    def get_button_text(self, text_to_be_present):
        return self.get_text(self.BUTTON_FOLLOW, text_to_be_present)

