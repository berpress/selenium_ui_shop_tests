from selenium.webdriver.common.by import By


class Authorization:
    LOGIN_BUTTON = (By.CLASS_NAME, 'header_user_info')
    LOGIN_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    SUBMIT_BUTTON = (By.ID, 'SubmitLogin')
    ERROR_AUTH_TEXT = (By.XPATH, '//*[@class="alert alert-danger"]')
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]/h3')
    LOGIN_HELPER_TEXT = (By.CLASS_NAME, 'form-group')
