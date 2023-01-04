from pom.main_page import MainPage
from pom.home_page import HomePage


class Pages:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.homepage = HomePage(driver)
