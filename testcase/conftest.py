import allure
import pytest
import requests
import time
from selenium import webdriver

# 测试方法级别的fixture装饰器，每个测试方法运行一次
@pytest.fixture(scope='function', autouse=False)
def api_fixture():
    s = requests.session()
    api_base_url = 'http://www.baidu.com'
    yield s, api_base_url
    s.close()


@pytest.fixture(scope='function', autouse=False)
def ui_fixture():
    global driver
    global ui_base_url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    ui_base_url = 'http://localhost:8080/'
    yield driver, ui_base_url
    time.sleep(5)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 在这里实行失败用例的截图
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        # 判断用例是失败状态则进行截图
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
