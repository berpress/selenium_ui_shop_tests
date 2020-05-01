import logging
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from common.utils import Elements
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

    def check_auth(self):
        elements = self.app.wd.find_elements(*Page.LOGIN_NAME)
        return len(elements)

    def get_all_products(self):
        """
        return all products on page
        """
        elements = self.app.wd.find_elements(*Page.PRODUCT)
        return elements

    def open_product(self, name: str):
        """
        open product by name
        """
        if not self.app.page_has_loaded():
            raise Exception('Page is not load')
        WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_element_located(
                Page.PRODUCT))
        products = self.get_all_products()
        for p in products:
            if name in p.text:
                action = ActionChains(self.app.wd)
                action.move_to_element(p).click().perform()
                Elements.try_to_click(p, Page.MORE_BUTTON)
                # button_more = p.find_element(*Page.MORE_BUTTON)
                # button_more.click()
                logger.info(f'Open card by product name: {name}')
                break

    def add_product_to_car(self):
        pass

    def woman_category(self):
        return self.app.wd.find_element(*Page.CATEGORY_WOMEN)

    def select_woman_category(self):
        self.woman_category().click()

    def get_product_info(self, product: WebElement):
        actions = ActionChains(self.app.wd)
        actions.move_to_element(product).click().perform()

    def product_name(self):
        return self.app.wd.find_element(*Page.PRODUCT_NAME).text

    def product_model(self):
        return self.app.wd.find_element(*Page.PRODUCT_MODEL).text

    def product_description(self):
        return self.app.wd.find_element(*Page.PRODUCT_DESCRIPTION).text

    def product_price(self):
        return self.app.wd.find_element(*Page.PRODUCT_PRICE).text

    @staticmethod
    def get_color(element):
        color = element.get_attribute("style")
        return color[12:]

    def black_color(self):
        return self.app.wd.find_element(*Page.BLACK)

    def orange_color(self):
        return self.app.wd.find_element(*Page.ORANGE)

    def blue_color(self):
        return self.app.wd.find_element(*Page.BLUE)

    def yellow_color(self):
        return self.app.wd.find_element(*Page.YELLOW)
