import pytest
import allure

class TestUILoin1:

    age = 16
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @allure.feature('uilogin')
    @allure.severity('blocker')
    def test_ui01(self):
        print('\ntest_ui01')

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @allure.feature('uilogin')
    @allure.severity('critical')
#    @pytest.mark.skip(reason='test case is not valid any more')
    def test_ui02(self,all_fixture,ui_fixture):
        print('\ntest_ui02')
        assert 2==2

    @pytest.mark.run(order=3)
    @pytest.mark.regression
    @allure.feature('uilogin')
    @allure.severity('normal')
 #   @pytest.mark.skipif(age<18, reason='age is younger than 18')
    def test_ui03(self):
        print('\ntest_ui03')



# class TestUILoin2:
#
#     age = 16
#     @pytest.mark.run(order=1)
#     @pytest.mark.smoke
#     def test_ui01(self):
#         print('\ntest_ui04')
#
#     @pytest.mark.run(order=2)
#     @pytest.mark.smoke
# #    @pytest.mark.skip(reason='test case is not valid any more')
#     def test_ui02(self,all_fixture):
#         print('\ntest_ui05')
#
#     @pytest.mark.run(order=3)
#     @pytest.mark.regression
#  #   @pytest.mark.skipif(age<18, reason='age is younger than 18')
#     def test_ui03(self):
#         print('\ntest_ui06')




