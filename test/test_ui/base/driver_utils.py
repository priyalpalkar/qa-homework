from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverUtils(object):

    _chrome_ajax_timeout = 10
    _chrome_js_timeout = 10

    def __init__(self, *args, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def execute_script(self, cmd):
        if self.driver.execute_script(cmd) == 0:
            return True
        return False

    def driver_wait_for_ajax(self, *args):
        return self.execute_script("return jQuery.active")

    def find_element(self, selector, type="CSS_SELECTOR", wait_for_ajax=True):
        if wait_for_ajax:
            self.wait_until(self.driver_wait_for_ajax, self._chrome_ajax_timeout)
        element = None
        element = self.wait_until(EC.presence_of_element_located((self._by_type(type), selector)), self._chrome_js_timeout)
        return element

    def wait_for_element_invisibility(self, selector, type="CSS_SELECTOR", wait_for_ajax=True):
        if wait_for_ajax:
            self.wait_until(self.driver_wait_for_ajax, self._chrome_ajax_timeout)
        element = None
        element = self.wait_until(EC.invisibility_of_element_located((self._by_type(type), selector)), self._chrome_js_timeout)
        return element

    def click(self, selector, type="CSS_SELECTOR", wait_for_ajax=True):
        element = self.wait_until(EC.element_to_be_clickable((self._by_type(type), selector)), self._chrome_js_timeout)
        element.click()
        if wait_for_ajax:
            self.wait_until(self.driver_wait_for_ajax, self._chrome_js_timeout)
        return True

    def wait_until(self, condition, timeout=10, error_message="Timeout!"):

        element = WebDriverWait(self.driver, timeout).until(condition, error_message)
        return element

    def find_elements(self, selector, type="CSS_SELECTOR", wait_for_ajax=True):
        if wait_for_ajax:
            self.wait_until(self.driver_wait_for_ajax, self._chrome_ajax_timeout)
        elements = []
        elements = self.wait_until(EC.presence_of_all_elements_located((self._by_type(type), selector)), self._chrome_js_timeout)
        return elements

    def send_keys(self, element, key, wait_for_ajax=True, ajax_timeout=None):
        ajax_timeout = ajax_timeout or self._chrome_ajax_timeout
        element.send_keys(key)
        if wait_for_ajax:
            self.wait_until(self.driver_wait_for_ajax, ajax_timeout)

    def _by_type(self, type):
        return getattr(By, type)

