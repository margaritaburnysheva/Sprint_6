from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        (WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        (WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def switch_to_window(self, locator):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self.find_element_with_wait(locator)

    def click_to_element_with_exceptions(self, locator):
        try:
            self.click_to_element(locator)
        except NoSuchElementException:
            pass

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        (WebDriverWait(self.driver, 10).
            until(expected_conditions.element_to_be_clickable(locator)))
