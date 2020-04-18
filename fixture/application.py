from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging

from common.logging import setup
from fixture.login_page import LoginPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url):
        setup('INFO')
        logger.setLevel('INFO')
        options: Options = Options()
        options.headless = False
        driver = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver, options=options)
        self.login = LoginPage(self)
        self.base_url = base_url

    def open_main_page(self):
        logger.info(f'Open {self.base_url}')
        self.wd.get(self.base_url)

    def destroy(self):
        logger.info('Quit app')
        self.wd.quit()
