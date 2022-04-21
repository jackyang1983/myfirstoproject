import pytest
import allure
import logging

from common.yaml_util import YamlUtil


class TestAppLogin:
    @pytest.mark.smoke
    @allure.feature('apilogin')
    @allure.severity('minor')
    def test_api01(self,all_fixture,api_fixture):
        print('test_api01')

    @pytest.mark.smoke
    @pytest.mark.parametrize('args',YamlUtil('./data/test_apilogin.yaml').read_yaml())
    @allure.feature('apilogin')
    @allure.severity('blocker')
    def test_api02(self,all_fixture,api_fixture,args):
        print(args['name'],args['age'])
        logging.debug('test')


    @pytest.mark.smoke
    @allure.feature('apilogin')
    @allure.severity('blocker')
    def test_api03(self,all_fixture,api_fixture):
        print('test_api03')
