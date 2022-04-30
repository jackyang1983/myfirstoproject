import pytest
import requests
import time
from selenium import webdriver


# #测试类模块的fixture装饰器，每个测试模块运行一次
# @pytest.fixture(scope='module',autouse=False)
# def module_fixture():
#     s = requests.session()
#     base_url = 'http://www.baidu.com'
#     yield s,base_url
#     print('\n这是测试模块的后置操作,一个py文件运行一次')
#
# #测试类级别的fixture装饰器，每个测试类运行一次
# @pytest.fixture(scope='class',autouse=False)
# def class_fixture():
#     print('\n这是测试类的前置操作,一个class文件运行一次')
#     yield
#     print('\n这是测试类的后置操作,一个class文件运行一次')

#测试方法级别的fixture装饰器，每个测试方法运行一次
@pytest.fixture(scope='function',autouse=False)
def api_fixture():
    s = requests.session()
    base_url = 'http://www.baidu.com'
    yield s,base_url
    s.close()

@pytest.fixture(scope='function',autouse=False)
def ui_fixture():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = 'http://www.baidu.com'
    yield driver,base_url
    time.sleep(5)
    driver.close()
