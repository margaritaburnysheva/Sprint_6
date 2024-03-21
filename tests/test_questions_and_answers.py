import pytest
import allure

from locators.main_page_locators import MainPageLocators
from constants import Constants
from pages.main_page import MainPage


class TestQuestionsAndAnswers:

    @allure.title('Проверка текста ответа в блоке "Вопросы о важном"')
    @allure.description('На главной странице в блоке "Вопросы о важном" кликнуть на стрелку с вопросом, проверить, что открывается соответствующий текст ответа')
    @pytest.mark.parametrize('num, expected_answer_text',
                             [
                                 [0, Constants.EXPECTED_ANSWER_TEXT_1],
                                 [1, Constants.EXPECTED_ANSWER_TEXT_2],
                                 [2, Constants.EXPECTED_ANSWER_TEXT_3],
                                 [3, Constants.EXPECTED_ANSWER_TEXT_4],
                                 [4, Constants.EXPECTED_ANSWER_TEXT_5],
                                 [5, Constants.EXPECTED_ANSWER_TEXT_6],
                                 [6, Constants.EXPECTED_ANSWER_TEXT_7],
                                 [7, Constants.EXPECTED_ANSWER_TEXT_8]
                             ])
    def test_questions_and_answers(self, driver, num, expected_answer_text):
        main_page = MainPage(driver)
        result = main_page.get_answer_text(MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, num)
        assert result == expected_answer_text, "Текст ответа не соответствует ожидаемому"
