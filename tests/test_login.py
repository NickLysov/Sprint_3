from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import Locators


class TestStellarburgersLogin:
    def test_login_login_button(self, driver):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('UserTest@UserTest.com')
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('UserTest123')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'


    def test_login_lk_button(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('UserTest@UserTest.com')
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('UserTest123')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'


    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.REGISTRATION_FIELD_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.NAME_FIELD))
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTARTION_PANEL).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('UserTest@UserTest.com')
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('UserTest123')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'


    def test_login_from_restore_password_page(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.FORGOT_PASSWORD_PANEL_OPEN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.FORGOT_PASSWORD_BUTTON))
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTARTION_PANEL).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('UserTest@UserTest.com')
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('UserTest123')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'
