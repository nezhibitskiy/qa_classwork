import random
from ui.base_case import BaseCase


class TestProfileNotification(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/notifications'

    def test_change_notifications(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, 15)
        
        elemets = self.base_page.find_all_elemets(self.profile_page.locators.NOTIFICATIONS,15)
        expected = self.profile_page.get_notifications_status(elemets)

        pos_to_swicth = [0,1,2,9]

        for pos in pos_to_swicth:
            expected[pos] = not expected[pos]
            self.base_page.elem_click(elemets[pos], 15)

        self.base_page.click(self.profile_page.locators.SAVE_NOTIFICATIONS, 15)
        self.base_page.wait_visability_of_elem(self.profile_page.locators.SUCCESS_SAVE_NOTIFICATIONS, 15)

        result = self.profile_page.get_notifications_status(elemets)

        assert expected == result


class TestProfileContacts(BaseCase):
    authorize = True
    url = 'https://target-sandbox.my.com/profile/contacts'
    
    def test_change_personal_data(self):
        self.driver.get(self.url)
        self.base_page.is_opened(self.url, 15)

        input_field = self.base_page.find(self.profile_page.locators.CONTACT_INPUT_FIELD, 15)

        if input_field.get_attribute('value') != "":
            expected = list(input_field.get_attribute('value'))
            expected[0] = chr(
                (int(expected[0])+1) % 10 + ord('0'))
            expected=''.join(expected)
        else:
            expected = 'test_data'

        self.base_page.send_keys(input_field, expected)

        self.base_page.click(
            self.profile_page.locators.SAVE_CONTACTS, 15)

        self.base_page.wait_visability_of_elem(
            self.profile_page.locators.SUCCESS_SAVE_CONTACTS, 15)

        updated_input_field = self.base_page.find(self.profile_page.locators.CONTACT_INPUT_FIELD, 15)
        assert updated_input_field.get_attribute('value') == expected