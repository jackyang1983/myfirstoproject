import pytest

from pageobj.dashboard_page import DashboardPage
from pageobj.login_page import LoginPage


class TestAddProj:

    @pytest.mark.smoke
    def test_01_addproj(self, start_driver):
        driver = start_driver
        LP = LoginPage(driver)
        LP.login_jenkins("admin", "admin")
        DP = DashboardPage(driver)
        DP.add_proj()


