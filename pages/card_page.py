import time
from base.base_class import Base
from locators.card_locators import CardLocators
from faker import Faker


class Card_page(Base):
    locators = CardLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()

    # Methods
    def input_data(self):
        # Generation of fake data
        first_name_fake = self.fake.name()
        street_name = self.fake.street_name()
        zip_code_fake = self.fake.postcode()
        city = self.fake.city()
        phone_number = self.fake.phone_number()
        email = self.fake.free_email()

        self.element_to_be_clickable(self.locators.delivery_button).click()
        print("Click Delivery")
        self.element_to_be_clickable(self.locators.not_login).click()
        self.element_to_be_clickable(self.locators.first_last_name).send_keys(first_name_fake)
        self.element_to_be_clickable(self.locators.street_home).send_keys(street_name)
        self.element_to_be_clickable(self.locators.zip_code).send_keys(zip_code_fake)
        self.element_to_be_clickable(self.locators.city).send_keys(city)
        self.element_to_be_clickable(self.locators.phone_number).send_keys(phone_number)
        self.element_to_be_clickable(self.locators.email).send_keys(email)
        print('Input data')
