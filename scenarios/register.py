import unittest
import time
import os

from selenium import webdriver
from ddt import ddt, data, unpack


from library.getData import getDatafromxls
from library.getscreenshoot import getScreenShotspath


@ddt
class Register(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.screenshotDir = getScreenShotspath()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @data(*getDatafromxls('./data/user.xls'))
    @unpack
    def test_login(self,username,passwd,status,excpetVal):
        dr = self.driver
        dr.get("http://118.31.19.120:3000/")
        dr.find_element_by_css_selector('body > div.navbar > div > div > ul > li:nth-child(6) > a').click()
        dr.find_element_by_id('name').send_keys(username)
        dr.find_element_by_id('pass').send_keys(passwd)

        dr.find_element_by_css_selector(".span-primary").click()

        if status == "成功":
            successText = dr.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
            self.assertEqual(successText,excpetVal)
        else:
            faildeText = dr.find_element_by_css_selector('#content > div > div.inner > div > strong').text
            self.assertEqual(faildeText,excpetVal)

    def tearDown(self):
        filename = str(time.time()) +".png"
        self.driver.save_screenshot(os.path.join(self.screenshotDir,filename))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()








