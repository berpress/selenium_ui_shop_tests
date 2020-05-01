import time

from selenium.common.exceptions import StaleElementReferenceException


class Elements:
    @staticmethod
    def try_to_click(element,  locator, wait_time=5):
        """
        Trying to click on an item over time
        """
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            try:
                elem = element.find_element(*locator)
                elem.click()
                return
            except StaleElementReferenceException:
                time.sleep(0.5)
