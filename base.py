import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service("C:\\Users\\97250\\Downloads\chromedriver_win32\\chromedriver.exe"))
driver.get('https://buyme.co.il/')


class Functions():

    def click_on_element(self,locator):
        driver.find_element().click()

    def enter_text(self,locator,text):
        driver.find_element().send_keys(text)

    def link_to_url(self, link):
        driver.get(link)


def __init__(self, driver):
    return None
