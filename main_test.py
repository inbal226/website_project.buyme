import unittest
import time
import base

from PIL import Image
from selenium.webdriver.common.by import By
from base import driver
from pages.gift_page import Home_screen
from pages.intro_page import Intro_screen
from pages.sender_and_resiver_page import Sender_and_receiver_screen


class Test_login_Buy_me(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.intro_page = Intro_screen(base.driver)
        self.gift_page = Home_screen(base.driver)
        self.sender_and_receiver_page = Sender_and_receiver_screen(base.driver)

    def test_register(self):
        # base.link_to_url(driver, base.datajson['url']['buyme'])
        self.intro_page.register()
    @classmethod
    def tearDownClass(self):
        driver.quit()

class Test_gift_card(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.intro_page = Intro_screen(base.driver)
        self.gift_page = Home_screen(base.driver)
        self.sender_and_receiver_page = Sender_and_receiver_screen(base.driver)


    def choose_a_gift(self):
        #base.link_to_url(driver, base.datajson['url']['buyme'])
        self.gift_page.choose_a_gift_card()

    @classmethod
    def tearDownClass(self):
        driver.quit()

class Test_send_gift(unittest.TestCase):
    @classmethod

    def setUp(self):
        self.intro_page = Intro_screen(base.driver)
        self.gift_page = Home_screen(base.driver)
        self.sender_and_receiver_page = Sender_and_receiver_screen(base.driver)

    def send_gift(self):
        #base.link_to_url(driver, base.datajson['url']['buyme'])
        self.sender_and_receiver_page.send_the_gift()

    @classmethod
    def tearDown(self):
        driver.quit()
