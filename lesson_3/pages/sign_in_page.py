class SignIn():

    def __init__(self, driver):
        self.driver = driver

    def create_account(self):
        self.driver.find_element_by_xpath("(//div[@role='button']/span)[2]").click()

    def create_account_for_you(self):
        self.driver.find_element_by_xpath("//div[@role='menu']//span[@role='menuitem']/div[2]/div").click()