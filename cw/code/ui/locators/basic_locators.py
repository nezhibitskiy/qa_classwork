from selenium.webdriver.common.by import By

class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    
    BUTTON_PRO = (By.XPATH, '//a[@href="/pro"]')
    BUTTON_PROFILE = (By.XPATH, '//a[@href="/profile"]')
    BUTTON_SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    BUTTON_BILLING = (By.XPATH, '//a[@href="/billing"]')
    BUTTON_TOOLS = (By.XPATH, '//a[@href="/tools"]')

class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//input[@name = "email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "password"]')
    PASS_LOGIN_CREDS_BUTTON = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')

class ProfilePageLocators(BasePageLocators):
    NOTIFICATION_THEMES = (By.XPATH, '//input[@class="profile__list__row__box js-mailing-item" and @type="checkbox"]')
    SAVE_NOTIFICATION_THEMES = (By.XPATH, '//div[@class="button__text" and text() = "Сохранить"]')
    SUCCESS_SAVE_NOTIFICATION_THEMES = (By.XPATH, '//div[@class="_notification__content js-notification-content" and text() = "Информация успешно сохранена"]')
    CONTACT_INN=(By.XPATH, '//div[@class="input" and @data-name = "ordInn"]/div/input')
    SAVE_CONTANTS = (By.XPATH, '//div[@class="button__text" and text() = "Сохранить"]')
    SUCCESS_SAVE_CONTACTS = (By.XPATH, '//div[@class="_notification__content js-notification-content" and text() = "Информация успешно сохранена"]')
