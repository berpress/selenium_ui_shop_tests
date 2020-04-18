from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Login:
    def __init__(self, app):
        self.app = app

    def password_input(self):
        return self.app.wd.find_element()

    def login_input(self):
        return self.app.wd.find_element()

    def login_button(self):
        return self.app.wd.find_element()

    def submit_login(self):
        return self.app.wd.find_element()

    def login(self, login, password, submit=True):
        self.login_button().click()
        self.login_input().send_keys(login)
        self.password_input().send_keys(password)
        if submit:
            self.submit_login().click()
