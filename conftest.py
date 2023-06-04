import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url)
    yield browser
    browser.quit()

