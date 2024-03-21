import datetime
import random
import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    def element_is_visibility(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator))

    def presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator))

    def element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator))

    def click_and_hold(self, locators, x, y):
        action = ActionChains(self.driver)
        action.click_and_hold(locators).move_by_offset(x, y).release().perform()

    def add_random_item_to_cart(self):
        available_items_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="listing-naglowek"]/div[1]')))

        available_items_text = available_items_element.text
        available_items_count = int(''.join(re.findall(r'\d+', available_items_text)))
        print(available_items_count)
        if available_items_count == 0:
            raise Exception("No items available to add to cart")

        random_item_index = str(random.randint(1, available_items_count))
        print(random_item_index)
        loc = (By.XPATH, f'//*[@id="listing-container"]/div[{random_item_index}]/div/div[2]/div[2]/div[1]/a/h3/span')
        return loc

    # Переход на url
    def url_trans(self, url):
        self.driver.get(url)

    # Функция возврата URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL {get_url}')

    # Функция проверки значения текста на странице
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")  # дата , время
        self.driver.save_screenshot(
            f'D:\\Testing\\OOPPytSel\\screen\\screenshot.{now_date}.png')  # делаем скриншот страницы
        print('Create screenshot')

    # Метод проверки URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value URL')
