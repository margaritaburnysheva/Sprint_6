import allure

from constants import Constants
from locators.dzen_locators import DzenLocators
from locators.header_and_cookie_locators import HeaderAndCookieLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class OrderStatusPage(BasePage):

    @allure.step('Перейти на страницу просмотра статуса заказа')
    def open_order_status_page(self, driver):
        driver.get(Constants.ORDER_STATUS_PAGE_URL)

    @allure.step('Кликнуть на лого "Самоката"')
    def click_to_scooter_logo(self):
        self.click_to_element(HeaderAndCookieLocators.SCOOTER_LOGO)
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step('Кликнуть на лого "Яндекса" с последующим переключением на новое окно')
    def click_to_yandex_logo(self):
        self.click_to_element(HeaderAndCookieLocators.YANDEX_LOGO)
        self.switch_to_window(DzenLocators.SEARCH_BUTTON)
