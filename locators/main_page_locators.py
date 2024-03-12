from selenium.webdriver.common.by import By


class MainPageLocators:
    agreement = (By.XPATH, '//button[@class="sc-15ih3hi-0 sc-1p1bjrl-9 gmtQwZ"]')
    computer = (By.XPATH, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[1]')
    phone_watch = (By.XPATH, '//*[@id="app"]/div[1]/header/div[2]/div/div/div/nav/ul/li[2]')
    gaming = (By.XPATH, "//a[@href='/g/7-gaming-i-streaming.html']")
    computer_kit = (By.XPATH, "//a[@href='/g/5-podzespoly-komputerowe.html']")
    optional_equipment = (By.XPATH, "//a[@href='/g/6-urzadzenia-peryferyjne.html']")
    tv_audio = (By.XPATH, "//a[@href='/g/8-tv-i-audio.html']")
    smarthome = (By.XPATH, "//a[@href='/g/64-smarthome-i-lifestyle.html']")
    accessories = (By.XPATH, "//a[@href='/g/12-akcesoria.html']")
    discounts = (By.XPATH, "//a[@href='/trendy']")
