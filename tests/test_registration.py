from fak12231er import Faker
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
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.NAME_FIELD_REGISTRATION))
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PSSWRD_FIELD_REGISTRATION).send_keys('psswrd')
        driver.find_element(*Locators.REGISTRATION_PUSH_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.EMAIL_FIELD_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASS_FIELD_AUTHORIZATION).send_keys('psswrd')
        driver.find_element(*Locators.ENTER_BUTTON_AUTH_FORM).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        assert driver.find_element(*Locators.CHECKOUT_ORDER).text == 'Оформить заказ'

    def test_registration_with_short_password(self, driver):
        email = fake.email()
        name = fake.name()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        driver.find_element(*Locators.REGISTRATION_FIELD_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.NAME_FIELD_REGISTRATION))
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PSSWRD_FIELD_REGISTRATION).send_keys('123')
        driver.find_element(*Locators.REGISTRATION_PUSH_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.WRONG_PASS_MESSAGE))
        assert driver.find_element(*Locators.WRONG_PASS_MESSAGE).text == 'Некорректный пароль'
