from selenium.webdriver.common.by import By


class OrderPageLocators:
    # локаторы для формы "Для кого самокат"
    NAME_FORM = (By.XPATH, './/*[@placeholder="* Имя"]')
    SURNAME_FORM = (By.XPATH, './/*[@placeholder="* Фамилия"]')
    ADDRESS_FORM = (By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]')
    SUBWAY_STATION_FORM = (By.XPATH, './/*[@placeholder="* Станция метро"]')
    SUBWAY_STATION_LIST = (By.XPATH, './/*[@class="select-search__select"]')
    PHONE_FORM = (By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT = (By.XPATH, './/*[text()="Далее"]')

    # локаторы для формы "Про аренду"
    DATE_FORM = (By.XPATH, './/*[@placeholder="* Когда привезти самокат"]')
    RENT_TIME_FORM = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENT_TIME_LIST = (By.CLASS_NAME, 'Dropdown-option')
    COMMENT_FOR_COURIER = (By.XPATH, './/*[@placeholder="Комментарий для курьера"]')
    FINISH_ORDER_BUTTON = (By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    CHECKBOX_GREY = (By.ID, 'grey')
    CHECKBOX_BLACK = (By.ID, 'black')

    # локаторы для подтверждения заказа
    ACCEPT_ORDER_BUTTON = (By.XPATH, './/*[text()="Да"]')
    ORDER_INFO = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
