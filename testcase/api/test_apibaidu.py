"""
this is api baidu test samples

"""
import pytest
import allure


class TestApiBaidu:

    @pytest.mark.smoke
    @allure.severity('low')
    def testbaidu(self, api_fixture):
        s, api_base_url = api_fixture
        result = s.get(api_base_url)
        print('this is baidu test')
        assert result.status_code == 200
