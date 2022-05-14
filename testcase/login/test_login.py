import pytest
import allure
from selenium.webdriver.common.by import By
from common.yaml_util import YamlUtil
from common.excel_util import ExcelUtil
from pageobj.login_page import LoginPage


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize('args', ExcelUtil('./data/test_case.xls', 'Sheet1').read_excel_to_list())
    # @pytest.mark.parametrize('args', YamlUtil('./data/test_uilogin.yaml').read_yaml())
    # @allure.severity('blocker')
    def test_01_login(self, args, start_driver):
        driver = start_driver
        LoginPage(driver).login_jenkins(args['username'], args['password'])
        flag = True
        try:
            driver.find_element(By.ID, 'search-box')
        except Exception as err:
            print(err)
            flag = False
        assert flag

