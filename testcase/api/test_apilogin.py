import pytest
import allure
import logging
from common.yaml_util import YamlUtil
from selenium import webdriver



class TestAppLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize('args',YamlUtil('./data/test_apilogin.yaml').read_yaml())
    @allure.severity('blocker')
    def test_baiduapi(self,api_fixture,args):
        s,base_url =  api_fixture
        result = s.get(base_url)
        assert result.status_code == 200

    # @pytest.mark.smoke
    # @allure.severity('blocker')
    # def test_baiduui(self,ui_fixture):
    #     driver,base_url =  ui_fixture
    #     driver.get(base_url)
    #     driver.find_element_by_id('kw').send_keys('iTesting')
    #     driver.find_element_by_id('su').click()
    #     search_result = driver.find_element_by_xpath('//*[@id="1"]/div/div[1]/h3/a').get_attribute('innerHTML')
    #     print(search_result)
    #     assert 'iTesting' in search_result