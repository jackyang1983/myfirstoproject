import time

import pytest

from pageobj.dashboard_page import DashboardPage
from pageobj.login_page import LoginPage
from pageobj.newproj_page import NewProjPage


class TestAddProj:

    @pytest.mark.smoke
    def test_01_addproj(self, start_driver):
        driver = start_driver
        LoginPage(driver).login_jenkins("admin", "admin")
        DashboardPage(driver).start_add_proj()
        NewProjPage(driver).create_proj("pytest")
        time.sleep(10)


