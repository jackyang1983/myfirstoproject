import pytest
import allure

class TestAppLogin:
    @pytest.mark.smoke
    @allure.feature('apilogin')
    @allure.severity('minor')
    def test_api01(self,all_fixture,api_fixture):
        print('test_api01')

