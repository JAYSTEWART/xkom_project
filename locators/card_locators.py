from selenium.webdriver.common.by import By


class CardLocators:
    delivery_button = (By.XPATH, '//button[@class="sc-15ih3hi-0 sc-d72h2o-4 epgAyb"]')
    not_login = (By.XPATH, '//button[@class="sc-15ih3hi-0 sc-zfvjto-6 bFlETZ"]')

    # User information locators
    user_private = (By.XPATH, '//input[@title="Osoba prywatna"]')
    firma = (By.XPATH, '//input[@title="Firma"]')
    first_last_name = (By.XPATH, '//input[@name="recipientName"]')
    street_home = (By.XPATH, '//input[@name="recipientStreet"]')
    zip_code = (By.XPATH, '//input[@name="recipientPostalCode"]')
    city = (By.XPATH, '//input[@name="recipientCity"]')
    phone_number = (By.XPATH, '//input[@name="recipientPhoneNumber"]')
    email = (By.XPATH, '//input[@name="recipientEmail"]')
