import logging

from locators.login import Authorization
from model.login import UserData

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

    def authorization(self, user: UserData, submit=True):
        logger.info(f'Try to login with login: {user.login} and password: '
                    f'{user.password}')
        self.login_button().click()
        self.login_input().send_keys(user.login)
        self.password_input().send_keys(user.password)
        if submit:
            self.submit_login().click()
