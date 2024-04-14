from selenium.webdriver.common.by import By


class HeaderAndCookieLocators:

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    SCOOTER_LOGO = (By.XPATH, './/*[@alt="Scooter"]')
    YANDEX_LOGO = (By.XPATH, './/*[@alt="Yandex"]')
