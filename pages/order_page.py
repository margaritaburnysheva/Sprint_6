import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить данные на форме "Для кого самокат" и перейти на форму "Про аренду"')
    def create_about_customer_form(self, name, surname, address, subway_station, phone):
        self.add_text_to_element(OrderPageLocators.NAME_FORM, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_FORM, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FORM, address)
        self.add_text_to_element(OrderPageLocators.SUBWAY_STATION_FORM, subway_station)
        self.click_to_element(OrderPageLocators.SUBWAY_STATION_LIST)
        self.add_text_to_element(OrderPageLocators.PHONE_FORM, phone)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнить данные на форме "Про аренду" и подтвердить оформление заказа')
    def create_about_rent_form(self, date, color_locator, comment):
        self.add_text_to_element(OrderPageLocators.DATE_FORM, date)
        self.click_to_element(color_locator)
        self.click_to_element(OrderPageLocators.RENT_TIME_FORM)
        self.click_to_element(OrderPageLocators.RENT_TIME_LIST)
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER, comment)
        self.click_to_element(OrderPageLocators.FINISH_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ACCEPT_ORDER_BUTTON)

    @allure.step('Получить текст подтверждения заказа')
    def check_order_info(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_INFO)
