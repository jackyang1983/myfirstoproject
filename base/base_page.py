from selenium import webdriver


class BasePage:
    driver = webdriver.Chrome()

    # def __init__(self,driver):
    #   self.dirver = driver


    def openpage(self,url):
        self.driver.get(url)

    def locate_element(self,args):
        return self.driver.find_element(args)

    def send_keys(self,args,value):
        self.locate_element(args).send_keys(value)

    def click(self,args):
        self.locate_element(args).click()



