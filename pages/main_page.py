import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получить текст ответа')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Выбрать кнопку "Заказать" на главной странице и нажать на нее')
    def click_order_button(self, order_button_main_page):
        if order_button_main_page == MainPageLocators.ORDER_BUTTON_DOWN:
            self.scroll_to_element(order_button_main_page)
            self.click_to_element(order_button_main_page)
            self.find_element_with_wait(OrderPageLocators.NAME_FORM)
        else:
            self.click_to_element(order_button_main_page)
            self.find_element_with_wait(OrderPageLocators.NAME_FORM)
