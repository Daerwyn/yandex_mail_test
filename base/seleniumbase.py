from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import random
import string


class SeleniumBase:

    def __init__(self, driver):
        self.random_text = None
        self.symbols = string.ascii_letters.lower() + " "*10
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, 0.3)

    def text_generate(self, length):
        self.random_text = ''.join(random.choice(self.symbols) for _ in range(length))
        return string.capwords(self.random_text)

    def _is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))

    def _is_invisible(self, locator):
        return self.wait.until(ec.invisibility_of_element_located((By.XPATH, locator)))

    def _are_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, locator)))

    def _is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))