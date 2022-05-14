from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    # 页面元素定位
    username_loc = (By.ID, "j_username")
    password_loc = (By.NAME, "j_password")
    submitbtn_loc = (By.NAME, "Submit")

    # 页面元素动作
    def login_jenkins(self, username, password):
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.click(self.submitbtn_loc)
