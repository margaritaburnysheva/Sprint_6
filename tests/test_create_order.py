import pytest
import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.header_and_cookie_page import HeaderAndCookiePage
from pages.order_page import OrderPage


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Заполнить данные заказа, подтвердить его оформление и проверить, что во всплывающем окне есть текст "Заказ оформлен"')
    @pytest.mark.parametrize('order_button_locator, name, surname, address, subway_station, phone, date, color_locator, comment',
                             [[MainPageLocators.ORDER_BUTTON_UP, 'Вася', 'Петров', 'Москва, Апрельская, 9999', 'Университет',
                               '79020000000', '01.01.2025', OrderPageLocators.CHECKBOX_GREY, 'Тестовый комментарий'],
                             [MainPageLocators.ORDER_BUTTON_DOWN, 'Маша', 'Иванова', 'Апрельская, 9999', 'Универ',
                              '79999999999', '01.01.2555', OrderPageLocators.CHECKBOX_BLACK, '']])
    def test_create_order(self, driver, order_button_locator, name, surname, address, subway_station, phone, date, color_locator, comment):
        main_page = MainPage(driver)
        header_and_cookie_page = HeaderAndCookiePage(driver)
        header_and_cookie_page.click_cookie_button()
        order_page = OrderPage(driver)
        main_page.click_order_button(order_button_locator)
        order_page.create_about_customer_form(name, surname, address, subway_station, phone)
        order_page.create_about_rent_form(date, color_locator, comment)
        result = order_page.check_order_info()
        assert 'Заказ оформлен' in result, 'Ошибка при оформлении заказа'
