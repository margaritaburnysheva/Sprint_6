import allure

from locators.header_and_cookie_locators import HeaderAndCookieLocators
from pages.base_page import BasePage


class HeaderAndCookiePage(BasePage):

    @allure.step('Принять куки')
    def click_cookie_button(self):
        self.click_to_element_with_exceptions(HeaderAndCookieLocators.COOKIE_BUTTON)
