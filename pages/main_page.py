from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.computer_page_locators import ComputerPageLocators
from base.base_class import Base


class Main_page(Base):
    url = 'https://www.x-kom.pl/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = MainPageLocators
    locators2 = ComputerPageLocators

    # Methods

    def get_computer(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.element_to_be_clickable(self.locators.agreement).click()
        self.element_to_be_clickable(self.locators.computer).click()
        self.element_to_be_clickable(self.locators2.computer_notebook).click()
