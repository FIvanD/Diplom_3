import allure
from data import Credentials
from pages.base_page import BasePage
from locators.auth_page_locators import AuthorizationPageLoc


class AuthPage(BasePage):

    @allure.step('Заполнение полей почты/пароль при авторизации и клик по кнопке войти')
    def add_auth_field_click(self, email: str = Credentials.EMAIL,
                             password: str = Credentials.PASSWORD):
        self.add_text_to_element(AuthorizationPageLoc.EMAIL_INPUT, email)
        self.add_text_to_element(AuthorizationPageLoc.PASS_INPUT, password)
        self.click_to_element(AuthorizationPageLoc.AUTH_BUTTON)


    @allure.step('Поиск кнопки войти')
    def find_log_button(self):
        self.find_element_with_wait(AuthorizationPageLoc.AUTH_BUTTON)