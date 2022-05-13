from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProjDashboard(BasePage):

    # 页面元素定位
    addproj_loc = (By.XPATH, '//*[@id="tasks"]/div[1]/span/a')

    # 页面元素动作
    def add_proj(self):
        self.click(self.addproj_loc)