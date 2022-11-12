import pytest
from ui.pages.base_page import BasePage
from ui.base_case import BaseCase
from ui.fixtures import base_page

class TestHeaderButtons(BaseCase):
    authorize = True

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            BasePage.locators.BUTTON_TOOLS, 
            'https://target-sandbox.my.com/tools'
        ),
        (
            BasePage.locators.BUTTON_PROFILE, 
            'https://target-sandbox.my.com/profile'
        ),
        (
            BasePage.locators.BUTTON_BILLING, 
            'https://target-sandbox.my.com/billing'
        ),
        ])
    
    def test_page_switching(self, button_locator,expected_url):
        self.base_page.click(button_locator, 10)
        assert str(self.driver.current_url) == expected_url