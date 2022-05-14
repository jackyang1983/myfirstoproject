from selenium import webdriver

# 原则：任何可变值不能写死，需要参数化
class BasePage:
    # driver = webdriver.Chrome()

    # 初始化浏览器窗口
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def locate_element(self, args):
        return self.driver.find_element(*args)

    # 输入值
    def send_keys(self, args, value):
        self.locate_element(args).send_keys(value)

    # 点击
    def click(self, args):
        self.locate_element(args).click()
