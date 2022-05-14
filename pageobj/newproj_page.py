from selenium.webdriver.common.by import By

from base.base_page import BasePage


class NewProjPage(BasePage):
    projname_loc = (By.ID, "name")
    proj_type_loc = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[1]')
    createprojbtn_loc = (By.XPATH, '//*[@id="createItem"]/div[4]/div/span')

    def create_proj(self, value):
        self.send_keys(self.projname_loc, value)
        self.click(self.proj_type_loc)
        self.click(self.createprojbtn_loc)
