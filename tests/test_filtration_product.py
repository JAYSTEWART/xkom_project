import time
from selenium import webdriver

from pages.card_page import Card_page
from pages.computer_page import Computer_page
from pages.main_page import Main_page

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/23.9.0.2325 Yowser/2.5 Safari/537.36'
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
options.add_argument(f'user-agent={user_agent}')


def test_buy_product_1():
    driver = webdriver.Chrome(options=options)

    print('Start Test')

    mp = Main_page(driver)
    mp.get_computer()

    cp = Computer_page(driver)
    cp.select_computer()

    cardp = Card_page(driver)
    cardp.input_data()

    time.sleep(10)
    print('Finish test')
