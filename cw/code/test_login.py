import time
import pytest

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By

from ui.fixtures import get_driver
from ui.fixtures import cookies
from ui.fixtures import credentials
from ui.base_case import BaseCase

from ui.pages.base_page import BasePage

class TestLogin(BaseCase):

    def test_lk1(self):
        time.sleep(5)

    def test_lk2(self):
        time.sleep(5)

