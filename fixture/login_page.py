import logging

from locators.login import Authorization
from model.login import UserData

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def _password_input(self):
        return self.app.wd.find_element(*Authorization.PASSWORD_INPUT)

    def _login_input(self):
        return self.app.wd.find_element(*Authorization.LOGIN_INPUT)

    def _login_button(self):
        return self.app.wd.find_element(*Authorization.LOGIN_BUTTON)

    def sign_button_click(self):
        self._login_button().click()

    def _submit_login(self):
        return self.app.wd.find_element(*Authorization.SUBMIT_BUTTON)

    def authentication(self, user: UserData, submit=True):
        logger.info(f'Try to login with login: {user.login} and password: '
                    f'{user.password}')
        self.sign_button_click()
        if user.login is not None:
            self._login_input().send_keys(user.login)
        if user.password is not None:
            self._password_input().send_keys(user.password)
        if submit:
            self._submit_login().click()

    def error_auth_text(self):
        return self.app.wd.find_element(*Authorization.ERROR_AUTH_TEXT).text

    def _login_form(self):
        return self.app.wd.find_element(*Authorization.LOGIN_FORM)

    def login_form_text(self):
        return self._login_form().text

    def helper_login(self):
        return self.app.wd.find_elements(*Authorization.LOGIN_HELPER_TEXT)
