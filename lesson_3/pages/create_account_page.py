class CreateAccount():

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname):
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id("lastName").send_keys(lastname)

    def enter_username(self, username):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

    def enter_confirmpassword(self, confirmpassword):
        self.driver.find_element_by_name("ConfirmPasswd").clear()
        self.driver.find_element_by_name("ConfirmPasswd").send_keys(confirmpassword)

    def click_next(self):
        self.driver.find_element_by_id("accountDetailsNext").click()
