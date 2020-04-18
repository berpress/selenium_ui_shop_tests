import logging

from locators.main_page import MainPage as Page

logger = logging.getLogger()


class MainPage:
    def __init__(self, app):
        self.app = app

    def login_name_text(self) -> str:
        return self.login_name().text

    def login_name(self):
        return self.app.wd.find_element(*Page.LOGIN_NAME)

    def logout_btn(self):
        return self.app.wd.find_element(*Page.LOGOUT)

    def logout_user(self):
        self.logout_btn().click()
