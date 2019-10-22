from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Валерия/Desktop/chromedriver.exe")

driver.get("https://wikipedia.org")
search_field = driver.find_element_by_id("searchInput")
search_field.send_keys("Test automamtion")
search_button = driver.find_element_by_xpath("//div[@id='search-input']/following-sibling::button")
search_button.click()
assert "Test automamtion" in driver.title
driver.quit()
