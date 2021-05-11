# coding = utf-8
import pytest
from selenium import webdriver
from  time import ctime,sleep
import os
option=webdriver.ChromeOptions()
option.binary_location = "C:/Users/86152/AppData/Local/Google/Chrome/Application/chrome.exe"
#chrome软件执行地址
chrome_driver_binary= "C:/Users/86152/AppData/Local/Google/Chrome/Application/chromedriver.exe"
  #驱动地址

browser=webdriver.Chrome(chrome_driver_binary,chrome_options=option)




class TestCase():
    def setup_class(self):
        print("\n setup_class：所有⽤例执⾏之前")
    def teardown_class(self):
        print("\n teardown_class：所有⽤例执⾏之后")
        browser.quit()
    def setup_method(self):
        browser.get("http://www.baidu.com")
        sleep(3)
        # setup_method: 每个⽤例开始前执⾏
    def teardown_method(self):
        sleep(3)
        
        # teardown_method: 每个⽤例结束后执⾏
    def test_one(self):
        print("\n 正在执⾏测试类----test_one")
        browser.find_element_by_id("kw").send_keys("Test search")
        browser.find_element_by_id("su").click()
    def test_two(self):
        print("\n 正在执⾏测试类----test_two")
        browser.find_element_by_id("kw").send_keys(" ")
        browser.find_element_by_id("su").click()
    def test_three(self):
        print("\n 正在执⾏测试类----test_three")
        browser.find_element_by_id("kw").send_keys("语文")
        browser.find_element_by_id("su").click()

    # def test_four(self):
    #     print("\n 正在执⾏测试类----test_four")