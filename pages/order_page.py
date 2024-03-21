import allure

from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Создать заказ: заполнить данные и подтвердить оформление')
    def create_order(self, name_locator, name,
                     surname_locator, surname,
                     address_locator, address,
                     subway_station_locator, subway_station,
                     subway_station_list_locator,
                     phone_locator, phone,
                     button_next_locator,
                     date_locator, date,
                     rent_time_locator,
                     rent_time_list_locator,
                     color_locator,
                     comment_locator, comment,
                     finish_order_button_locator,
                     accept_order_button_locator):
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(surname_locator, surname)
        self.add_text_to_element(address_locator, address)
        self.add_text_to_element(subway_station_locator, subway_station)
        self.click_to_element(subway_station_list_locator)
        self.add_text_to_element(phone_locator, phone)
        self.click_to_element(button_next_locator)
        self.add_text_to_element(date_locator, date)
        self.click_to_element(color_locator)
        self.click_to_element(rent_time_locator)
        self.click_to_element(rent_time_list_locator)
        self.add_text_to_element(comment_locator, comment)
        self.click_to_element(finish_order_button_locator)
        self.click_to_element(accept_order_button_locator)

    @allure.step('Получить текст подтверждения заказа')
    def check_order_info(self, locator):
        order_info = self.get_text_from_element(locator)
        return order_info
