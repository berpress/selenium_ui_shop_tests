from selenium.webdriver.common.by import By


class MainPage:
    LOGIN_NAME = (By.CLASS_NAME, 'account')
    LOGOUT = (By.CLASS_NAME, 'logout')
    PRODUCT = (By.CLASS_NAME, 'product-container')
    CATEGORY_WOMEN = (By.XPATH, '//*[@title="Women"]')
    MORE_BUTTON = (By.XPATH, './/*[@class="button lnk_view btn btn-default"]')
    PRODUCT_NAME = (By.XPATH,
                    '//*[@class="pb-center-column col-xs-12 col-sm-4"]/h1')
    PRODUCT_MODEL = (By.XPATH, '//*[@id="product_reference"]/span')
    PRODUCT_DESCRIPTION = (By.ID, 'short_description_content')
    PRODUCT_PRICE = (By.ID, 'our_price_display')
    LOGO = (By.ID, 'header_logo')
    BLACK = (By.NAME, 'Black')
    ORANGE = (By.NAME, 'Orange')
    BLUE = (By.NAME, 'Blue')
    YELLOW = (By.NAME, 'Yellow')
