import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.computer_page_locators import ComputerPageLocators
from base.base_class import Base


class Tablet_page(Base):
    locators = ComputerPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Actions
    def click_charging_cable(self):
        self.element_to_be_clickable(self.locators.charging_cable).click()
        print("Click Charging cable")

    def click_type_show_all(self):
        self.element_to_be_clickable(self.locators.type_show_all).click()
        print("Click Snow all")

    def click_brand_by(self):
        self.element_to_be_clickable(self.locators.brand_by).click()
        print("Click BY")

    def hold_price(self):
        self.click_and_hold(self.element_to_be_clickable(self.locators.price), 20, 0)
        print('Hold price')

    def add_product_1_to_card(self):
        self.element_to_be_clickable(self.locators.product_1).click()
        print('Add product to card')

    # Methods
    def select_charging_cable(self):
        self.click_type_show_all()
        self.click_charging_cable()
        self.click_brand_by()
        time.sleep(3)
        self.hold_price()
        self.add_product_1_to_card()
        time.sleep(5)
