from selenium.webdriver.common.by import By


class MainPageLocators:

    # локаторы для блока "Вопросы о важном"
    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')
    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')

    # локаторы для кнопок "Заказать"
    ORDER_BUTTON_UP = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_DOWN = (By.XPATH, './/*[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
