import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        (WebDriverWait(self.driver, 10).
            until(expected_conditions.element_to_be_clickable(locator)))

    @allure.step('Получить текст ответа')
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        element = self.find_element_with_wait(locator_q_formatted)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Выбрать кнопку "Заказать" на главной странице и нажать на нее')
    def click_order_button(self, order_button_main_page, locator_order_button_down, expected_element):
        if order_button_main_page == locator_order_button_down:
            self.scroll_to_element(order_button_main_page)
            self.click_to_element(order_button_main_page)
            self.find_element_with_wait(expected_element)
        else:
            self.click_to_element(order_button_main_page)
            self.find_element_with_wait(expected_element)
