import pytest
import allure

from locators.header_and_cookie_locators import HeaderAndCookieLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.header_and_cookie_page import HeaderAndCookiePage
from pages.order_page import OrderPage


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Заполнить данные заказа, подтвердить его оформление и проверить, что во всплывающем окне есть текст "Заказ оформлен"')
    @pytest.mark.parametrize('order_button_locator, name_locator, name, surname_locator, surname, address_locator, address, subway_station_locator, subway_station, subway_station_list_locator, phone_locator, phone, button_next_locator, date_locator, date, rent_time_locator, rent_time_list_locator, color_locator, comment_locator, comment, finish_order_button_locator, accept_order_button_locator',
                             [[MainPageLocators.ORDER_BUTTON_UP, OrderPageLocators.NAME_FORM, 'Вася',
                               OrderPageLocators.SURNAME_FORM, 'Петров', OrderPageLocators.ADDRESS_FORM, 'Москва, Апрельская, 9999',
                               OrderPageLocators.SUBWAY_STATION_FORM, 'Университет', OrderPageLocators.SUBWAY_STATION_LIST,
                               OrderPageLocators.PHONE_FORM, '79020000000', OrderPageLocators.BUTTON_NEXT,
                               OrderPageLocators.DATE_FORM, '01.01.2025', OrderPageLocators.RENT_TIME_FORM, OrderPageLocators.RENT_TIME_LIST,
                               OrderPageLocators.CHECKBOX_GREY, OrderPageLocators.COMMENT_FOR_COURIER, 'Тестовый комментарий',
                               OrderPageLocators.FINISH_ORDER_BUTTON, OrderPageLocators.ACCEPT_ORDER_BUTTON],
                             [MainPageLocators.ORDER_BUTTON_DOWN, OrderPageLocators.NAME_FORM, 'Маша',
                              OrderPageLocators.SURNAME_FORM, 'Иванова', OrderPageLocators.ADDRESS_FORM, 'Апрельская, 9999',
                              OrderPageLocators.SUBWAY_STATION_FORM, 'Универ', OrderPageLocators.SUBWAY_STATION_LIST,
                              OrderPageLocators.PHONE_FORM, '79999999999', OrderPageLocators.BUTTON_NEXT,
                              OrderPageLocators.DATE_FORM, '01.01.2555', OrderPageLocators.RENT_TIME_FORM, OrderPageLocators.RENT_TIME_LIST,
                              OrderPageLocators.CHECKBOX_BLACK, OrderPageLocators.COMMENT_FOR_COURIER, '',
                              OrderPageLocators.FINISH_ORDER_BUTTON, OrderPageLocators.ACCEPT_ORDER_BUTTON]])
    def test_create_order(self, driver, order_button_locator, name_locator, name, surname_locator, surname, address_locator, address,
                     subway_station_locator, subway_station, subway_station_list_locator, phone_locator, phone, button_next_locator,
                     date_locator, date, rent_time_locator, rent_time_list_locator, color_locator, comment_locator, comment,
                     finish_order_button_locator, accept_order_button_locator):
        main_page = MainPage(driver)
        header_and_cookie_page = HeaderAndCookiePage(driver)
        header_and_cookie_page.click_cookie_button(HeaderAndCookieLocators.COOKIE_BUTTON)
        order_page = OrderPage(driver)
        main_page.click_order_button(order_button_locator, MainPageLocators.ORDER_BUTTON_DOWN, name_locator)
        order_page.create_order(name_locator, name, surname_locator, surname, address_locator, address,
                     subway_station_locator, subway_station, subway_station_list_locator, phone_locator, phone,
                     button_next_locator, date_locator, date, rent_time_locator, rent_time_list_locator, color_locator,
                     comment_locator, comment, finish_order_button_locator, accept_order_button_locator)
        result = order_page.check_order_info(OrderPageLocators.ORDER_INFO)
        assert 'Заказ оформлен' in result, 'Ошибка при оформлении заказа'
