import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options

from pom.pages import Pages


@pytest.fixture(scope='class')
def get_chrome_options():
    options = Chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    return options


@pytest.fixture(scope='class')
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='C:\\bin\\chromedriver.exe', options=options)
    return driver


@pytest.fixture()
def ui(get_webdriver):
    yield Pages(get_webdriver)


@pytest.fixture(scope='class')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://mail.yandex.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
