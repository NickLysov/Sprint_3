import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import Locators

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
    driver.find_element(*Locators.EMAIL_FIELD_AUTHORIZATION).send_keys('UserTest@UserTest.com')
    driver.find_element(*Locators.PASS_FIELD_AUTHORIZATION).send_keys('UserTest123')
    driver.find_element(*Locators.ENTER_BUTTON_AUTH_FORM).click()
    return driver
