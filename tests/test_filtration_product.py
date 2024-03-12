import time
from selenium import webdriver

from pages.computer_page import Computer_page
from pages.main_page import Main_page


def test_buy_product_1():
    driver = webdriver.Chrome()

    print('Start Test')

    mp = Main_page(driver)
    mp.get_computer()

    cp = Computer_page(driver)
    cp.select_computer()

    time.sleep(5)
    print('Finish test')
