from selenium.webdriver.common.by import By


class BaseLocators:
    button_add_to_card = (By.XPATH, '//button[@data-name="addToBasketButton"]')

    close_button = (By.XPATH, '//button[@title="Zamknij"]')
    go_card = (By.XPATH, '//*[@id="react-portals"]/div[8]/div/div/div/div[3]/button[2]')
    card = (By.XPATH, '//div[@data-name="miniBasketTab"]')
