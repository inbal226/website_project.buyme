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
    to_who = driver.find_element(By.XPATH, value="//div[@gtm='למישהו אחר']")
    receiver_name = driver.find_element(By.XPATH, value="//input[contains(@class ,'ember-view ember-text-field')]")
    celebration = driver.find_element(By.XPATH, "//span[contains(@title, 'לאיזה אירוע')]")
    what_event = driver.find_element(By.XPATH, "//li[@value='11']")
    greeting_text = driver.find_element(By.XPATH, value="//textarea[@data-parsley-group='voucher-greeting']")
    upload_image = driver.find_element(By.XPATH, value="//input[@type='file']")
    continue_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
    send_by_sms = driver.find_element(By.CSS_SELECTOR, value= "path.circle")
    mobile_num = driver.find_element(By.ID, value="sms")
    sender_name =driver.find_element( By.XPATH,value= "//input[@placeholder='שם שולח המתנה']")
    sender_mobile = driver.find_element( By.XPATH,value= "//input[@placeholder='מספר נייד']")
    submit = driver.find_element(By.XPATH, '//span[contains@class,"label")]')

class Sender_and_receiver_screen(base):
    def __init__(self, driver):
        base.__init__(self, driver)
        self.driver = base.driver

    def send_the_gift(self):
        base.Functions.click_on_element(self,Constants.to_who)
        base.Functions.enter_text(Constants.receiver_name,"tamar")
        driver.implicitly_wait(2)
        base.Functions.click_on_element(Constants.celebration)
        base.Functions.click_on_element(self,Constants.what_event)
        driver.implicitly_wait(4)
        base.Functions.enter_text(self,Constants.greeting_text,"מזל טוב")
        base.Functions.enter_text(self,Constants.upload_image,"C:\\Users\\97250\\Desktop\\photo.jpg")
        driver.implicitly_wait(3)
        base.Functions.click_on_element(self,Constants.continue_button)
        driver.implicitly_wait(5)
        base.Functions.click_on_element(self,Constants.send_by_sms)
        driver.implicitly_wait(2)
        base.Functions.enter_text(self,Constants.mobile_num,"0508485766")
        driver.implicitly_wait(2)
        base.Functions.enter_text(self,Constants.sender_name,"inbal")
        base.Functions.enter_text(self,Constants.sender_mobile,"0679543399")
        driver.implicitly_wait(2)
        base.Functions.click_on_element(self,Constants.submit)


