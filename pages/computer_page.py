import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.computer_page_locators import ComputerPageLocators
from base.base_class import Base


class Computer_page(Base):
    locators = ComputerPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Actions
    def click_producer_hp(self):
        self.element_to_be_clickable(self.locators.producer_hp).click()
        print("Click Producer HP")

    def click_filters_gaming(self):
        self.element_to_be_clickable(self.locators.business).click()
        print("Click Gaming")

    def click_filters_os(self):
        self.element_to_be_clickable(self.locators.windows_11).click()
        print("Click Windows 11")

    def click_sale(self):
        self.element_to_be_clickable(self.locators.sale).click()
        print("Click Sale")

    # Methods
    def select_computer(self):
        self.click_producer_hp()
        self.click_filters_gaming()
        self.click_filters_os()
        self.click_sale()
