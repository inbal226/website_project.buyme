import time

from select import select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import base
from base import Functions
from base import driver




class Constants:
    price = base.driver.find_element(By.XPATH, value="//span[@title='סכום']")
    amount = driver.find_element(By.XPATH, value="//span[contains(text(), '100-199')]")
    erea = driver.find_element(By.XPATH, value="//span[@title='אזור']")
    erea_a = driver.find_element(By.XPATH, value="//span[text()='צפון']")
    category = driver.find_element(By.XPATH, value="//span[@title='קטגוריה']")
    category_a = driver.find_element(By.XPATH, value='//span[@class="selected-text"]')
    button_find_me_gift = driver.find_element(By.XPATH, value="//a[@rel='nofollow']")
    gift = driver.find_element(By.XPATH, value="//div[contains(@class, 'bm-product-card')]")
    card_sum = driver.find_element(By.XPATH, value='//input [contains(@placeholder, "הכנס סכום")]')
    button_submit = driver.find_element(By.XPATH, '//button[contains (@type,"submit")]')

class Home_screen(base):
    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base.driver


    def choose_a_gift_card(self):
        base.Functions.click_on_element(self,Constants.price)
        base.Functions.click_on_element(self,Constants.amount)
        driver.implicitly_wait(1)
        base.Functions.click_on_element(self,Constants.erea)
        base.Functions.click_on_element(self,Constants.erea_a)
        base.Functions.click_on_element(self,Constants.category)
        base.Functions.click_on_element(self,Constants.category_a)
        base.Functions.click_on_element(self,Constants.button_find_me_gift)
        driver.implicitly_wait(4)
        base.Functions.click_on_element(self,Constants.gift)
        driver.implicitly_wait(2)
        base.Functions.enter_text(self,Constants.card_sum,"150")
        base.Functions.click_on_element(self,Constants.button_submit)
        driver.implicitly_wait(2)


