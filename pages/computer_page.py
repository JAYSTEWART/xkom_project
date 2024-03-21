import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.computer_page_locators import ComputerPageLocators
from locators.base_locators import BaseLocators
from base.base_class import Base


class Computer_page(Base):
    locators = ComputerPageLocators()
    locators_base = BaseLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Actions
    # def click_producer_hp(self):
    #     self.element_to_be_clickable(self.locators.producer_hp).click()
    #     print("Click Producer HP")

    # def click_filters_gaming(self):
    #     self.element_to_be_clickable(self.locators.business).click()
    #     print("Click Gaming")

    # def click_filters_os(self):
    #     self.element_to_be_clickable(self.locators.windows_11).click()
    #     print("Click Windows 11")

    # def click_sale(self):
    #     self.element_to_be_clickable(self.locators.sale).click()
    #     print("Click Sale")

    # Methods
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
        self.element_to_be_clickable(self.locators_base.button_add_to_card).click()
        time.sleep(2)
        self.element_to_be_clickable(self.locators_base.close_button).click()
        time.sleep(5)
