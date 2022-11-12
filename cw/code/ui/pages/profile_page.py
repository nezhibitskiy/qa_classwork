from ui.locators import basic_locators
from ui.pages.base_page import BasePage

class ProfilePage(BasePage):
    locators = basic_locators.ProfilePageLocators()

    def get_notifications_status(self, notifications_elements):
        return list(map( lambda elem: elem.is_selected(),notifications_elements))
