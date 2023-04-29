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
        login= driver.find_element(By.CLASS_NAME, value="notSigned")
        registration= driver.find_element(By.XPATH, value="//span[@class='text-link theme']")
        first_name_input = base.driver.find_element(By.XPATH, "//input[@placeholder='שם פרטי']")
        email= driver.find_element(By.XPATH, value="//input[@ placeholder='מייל']" )
        password= driver.find_element(By.XPATH,value="//input[@placeholder='סיסמה']")
        repassword= driver.find_element(By.XPATH,value="//input[@placeholder='אימות סיסמה']")
        circle= driver.find_element(By.XPATH,value= "//span[@class='circle']")
        registration_button= driver.find_element(By.XPATH,value= "//button[@type='submit']")

class Intro_screen(base):
    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base.driver




    def register(self):
        base.Functions.click_on_element(self,Constants.login)
        driver.implicitly_wait(1)
        base.Functions.click_on_element(self,Constants.registration)
        driver.implicitly_wait(1)
        base.Functions.enter_text(self, Constants.first_name_input, "inbal")
        base.Functions.enter_text(self, Constants.email, "efhgh@walla.com")
        base. Functions.enter_text(self, Constants.password, "123Asdf@")
        base.Functions.enter_text(self, Constants.repassword, "123Asdf@")
        driver.implicitly_wait(1)
        base.Functions.click_on_element(self, Constants.circle)
        driver.implicitly_wait(1)
        base.Functions.click_on_element(self, Constants.registration_button)
