import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_result import SearchResult

# variables
instagram_page = "https://www.instagram.com/accounts/login/"
username = "valeria13_sh"
password = "tbc"
keywords = {"fitness"}

# set up driver
driver = webdriver.Chrome("C:/Users/Валерия/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.get(instagram_page)

login_page = LoginPage(driver)
login_page.enter_username(username)
login_page.enter_password(password)
login_page.click_submit()

main_page = MainPage(driver)
main_page.click_not_now_button()

for keyword_for_search in keywords:
    main_page.typein_search_field(keyword_for_search)
    main_page.click_search_result("#" + keyword_for_search)

    search_page = SearchResult(driver)
    time.sleep(5)
    assert "Подписаться" in search_page.get_button_text("Подписаться")

driver.quit()