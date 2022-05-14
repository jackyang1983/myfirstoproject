import allure
import pytest
from selenium import webdriver


driver = None

@pytest.fixture(scope='function', autouse=False)
def start_driver():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.implicitly_wait(5)
    yield driver
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
