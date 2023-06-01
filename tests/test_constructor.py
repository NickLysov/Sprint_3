from selenium.webdriver.common.by import By

from locators import Locators


class TestStellarburgersConstructor:
    def test_constructor_sous(self, driver):
        driver.find_element(*Locators.SOUS_CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]").text == "Соусы"


    def test_constructor_bulki(self, driver):
        driver.find_element(*Locators.SOUS_CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.BULKI_CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]").text == "Булки"


    def test_constructor_nachink(self, driver):
        driver.find_element(*Locators.NACHINKI_CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]").text == "Начинки"