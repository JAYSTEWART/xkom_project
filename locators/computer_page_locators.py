from selenium.webdriver.common.by import By


class ComputerPageLocators:
    # Locators groups
    computer_notebook = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]')
    computer_notebook_2w1 = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[4]')
    computer_notebook_business = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[6]')
    computer_desktop = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[8]')
    computer_G4M3R = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[10]')
    computer_tablet = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[12]')
    computer_server = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[14]')
    computer_programs = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[16]')
    computer_equipment = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[18]')
    computer_equipment_notebook = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[20]')
    computer_bags_cases = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[22]')
    computer_station = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[24]')

    # Notebook producer filter locators
    producer_hp = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[1]/div[1]/div')
    producer_asus = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[1]/div[2]')

    # Notebook Status filter locators
    discount = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[5]/div[1]')
    sale = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[5]/div[3]')

    # Product purpose filter locators
    science = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[7]/div[1]')
    universal = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[7]/div[2]')
    business = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[7]/div[3]')
    gaming = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[7]/div[4]')
    graphics = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[7]/div[5]')

    # System OS filter locators
    defectOS = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[9]/div[1]')
    windows_11 = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[9]/div[2]')
    windows_10 = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[9]/div[3]')
    macOS = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[9]/div[4]')
    chromeOS = (By.XPATH, '//*[@id="listing-filters"]/div[2]/div/section[9]/div[5]')

    first_item = (By.XPATH, '//*[@id="listing-container"]/div[1]/div/div[2]/div[2]/div[1]/a/h3/span')
