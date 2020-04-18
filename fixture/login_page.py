import logging

from locators.login import Authorization

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def password_input(self):
        return self.app.wd.find_element(*Authorization.PASSWORD_INPUT)

    def login_input(self):
        return self.app.wd.find_element(*Authorization.LOGIN_INPUT)

    def login_button(self):
        return self.app.wd.find_element(*Authorization.LOGIN_BUTTON)

    def submit_login(self):
        return self.app.wd.find_element(*Authorization.SUBMIT_BUTTON)

    def authorization(self, login, password, submit=True):
        logger.info(f'Try to login with login: {login} and password: '
                    f'{password}')
        self.login_button().click()
        self.login_input().send_keys(login)
        self.password_input().send_keys(password)
        if submit:
            self.submit_login().click()
