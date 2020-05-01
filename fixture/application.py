import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging

from common.logging import setup
from fixture.login_page import LoginPage
from fixture.main_page import MainPage

logger = logging.getLogger()


class Application:
    def __init__(self, base_url):
        setup('INFO')
        logger.setLevel('INFO')
        options: Options = Options()
        options.headless = True
        driver = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver, options=options)
        self.login = LoginPage(self)
        self.page = MainPage(self)
        self.base_url = base_url

    def open_main_page(self):
        logger.info(f'Open {self.base_url}')
        self.wd.get(self.base_url)

    def destroy(self):
        logger.info('Quit app')
        self.wd.quit()

    def get_url(self):
        return self.wd.current_url

    def page_has_loaded(self, wait_time=5) -> bool:
        """
        Waiting for the page to load.
        """
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            page_state = self.wd.execute_script('return document.readyState;')
            if page_state == 'complete':
                logger.info(f'Page {self.get_url()} is load')
                return True
            time.sleep(0.5)
        logger.info(f"Error, page {self.get_url()} isn't load")
        return False
