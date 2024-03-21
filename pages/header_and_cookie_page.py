import allure

from selenium.common import NoSuchElementException

from pages.base_page import BasePage


class HeaderAndCookiePage(BasePage):

    @allure.step('Принять куки')
    def click_cookie_button(self, cookie_locator):
        try:
            self.click_to_element(cookie_locator)
        except NoSuchElementException:
            pass
