import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.computer_page_locators import ComputerPageLocators
from locators.base_locators import BaseLocators
from base.base_class import Base


class Computer_page(Base):
    locators = ComputerPageLocators()
    base_locators = BaseLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    with allure.step('Select computer'):

        def select_computer(self):
            self.element_to_be_clickable(self.locators.producer_hp).click()
            print("Click Producer HP")
            time.sleep(1)

            self.element_to_be_clickable(self.locators.gaming).click()
            print("Click Gaming")
            time.sleep(1)

            self.element_to_be_clickable(self.locators.windows_11).click()
            print("Click Windows 11")
            time.sleep(1)

            self.element_to_be_clickable(self.locators.sale).click()
            print("Click Sale")
            time.sleep(1)

            self.element_to_be_clickable(self.add_random_item_to_cart()).click()
            self.element_to_be_clickable(self.base_locators.button_add_to_card).click()
            time.sleep(2)
            self.element_to_be_clickable(self.base_locators.close_button).click()
            self.element_to_be_clickable(self.base_locators.card).click()
            time.sleep(5)
