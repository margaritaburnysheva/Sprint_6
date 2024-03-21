import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class OrderStatusPage(BasePage):

    @allure.step('Кликнуть на лого без переключения на новое окно')
    def click_to_logo_without_window_switch(self, logo, expected_element):
        self.click_to_element(logo)
        (WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(expected_element)))

    @allure.step('Кликнуть на лого с последующим переключением на новое окно')
    def click_to_logo_with_window_switch(self, logo, expected_element):
        self.click_to_element(logo)
        self.switch_to_window(expected_element)
