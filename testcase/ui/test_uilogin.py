import pytest
import allure
import logging
from common.yaml_util import YamlUtil
from common.excel_util import ExcelUtil
from selenium import webdriver


class TestAppLogin:

    @pytest.mark.smoke
    # @pytest.mark.parametrize('args', YamlUtil('./data/test_uilogin.yaml').read_yaml())
    @pytest.mark.parametrize('args', ExcelUtil('./data/test_case.xls','Sheet1').read_exceltolist())
    @allure.severity('blocker')
    def test_jenkins(self, ui_fixture, args):
        driver, ui_base_url = ui_fixture
        driver.get(ui_base_url)
        try:
            driver.find_element_by_id('j_username').send_keys(args['username'])
            driver.find_element_by_name('j_password').send_keys(args['password'])
            driver.find_element_by_name('Submit').click()
            driver.find_element_by_id('search-box')
            flag = True
        except Exception as err:
            flag = False
            print('this is error:', err)
        assert flag

