from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators

fake = Faker("ru_RU")


class TestStellarburgersRegistration:
    def test_registration_with_normal_values(self, driver):
        email = fake.email()
        name = fake.name()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.REGISTRATION_FIELD_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.NAME_FIELD))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('psswrd')
        driver.find_element(*Locators.REGISTRATION_PUSH_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('psswrd')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'

    def test_registration_with_short_password(self, driver):
        email = fake.email()
        name = fake.name()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.REGISTRATION_FIELD_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.NAME_FIELD))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PSSWRD_FIELD).send_keys('123')
        driver.find_element(*Locators.REGISTRATION_PUSH_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.WRONG_PASS_MESSAGE))
        assert driver.find_element(*Locators.WRONG_PASS_MESSAGE).text == 'Некорректный пароль'
