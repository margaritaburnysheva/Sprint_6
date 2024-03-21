import allure

from locators.dzen_locators import DzenLocators
from locators.header_and_cookie_locators import HeaderAndCookieLocators
from locators.main_page_locators import MainPageLocators
from constants import Constants
from pages.order_status_page import OrderStatusPage


class TestLogoSwitchToPage:

    @allure.title('Проверка переключения на главную страницу по клику на лого "Самоката"')
    @allure.description('Нажать на логотип "Самоката", проверить, что попали на главную страницу "Самоката"')
    def test_check_switch_url_scooter(self, driver):
        status_page = OrderStatusPage(driver)
        driver.get(Constants.ORDER_STATUS_PAGE_URL)
        status_page.click_to_logo_without_window_switch(HeaderAndCookieLocators.SCOOTER_LOGO, MainPageLocators.ORDER_BUTTON_DOWN)
        assert driver.current_url == Constants.BASE_URL, 'По клику на лого "Самоката" не открывается главная страница "Самоката"'

    @allure.title('Проверка открытия главной страницы "Дзена" по клику на лого "Яндекса"')
    @allure.description('Нажать на логотип "Яндекса", проверить, что в новом окне через редирект откроется главная страница "Дзена"')
    def test_check_switch_url_yandex(self, driver):
        order_status_page = OrderStatusPage(driver)
        driver.get(Constants.ORDER_STATUS_PAGE_URL)
        order_status_page.click_to_logo_with_window_switch(HeaderAndCookieLocators.YANDEX_LOGO, DzenLocators.SEARCH_BUTTON)
        assert driver.current_url == Constants.DZEN_REDIRECT_URL, 'По клику на лого "Яндекса" не открывается главная страница "Дзена"'
