import allure

from constants import Constants
from pages.order_status_page import OrderStatusPage


class TestLogoSwitchToPage:

    @allure.title('Проверка переключения на главную страницу по клику на лого "Самоката"')
    @allure.description('Нажать на логотип "Самоката", проверить, что попали на главную страницу "Самоката"')
    def test_check_switch_url_scooter(self, driver):
        order_status_page = OrderStatusPage(driver)
        order_status_page.open_order_status_page(driver)
        order_status_page.click_to_scooter_logo()
        assert order_status_page.get_current_url(driver) == Constants.BASE_URL, 'По клику на лого "Самоката" не открывается главная страница "Самоката"'

    @allure.title('Проверка открытия главной страницы "Дзена" по клику на лого "Яндекса"')
    @allure.description('Нажать на логотип "Яндекса", проверить, что в новом окне через редирект откроется главная страница "Дзена"')
    def test_check_switch_url_yandex(self, driver):
        order_status_page = OrderStatusPage(driver)
        order_status_page.open_order_status_page(driver)
        order_status_page.click_to_yandex_logo()
        assert order_status_page.get_current_url(driver) == Constants.DZEN_REDIRECT_URL, 'По клику на лого "Яндекса" не открывается главная страница "Дзена"'
