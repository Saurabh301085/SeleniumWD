import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_javascript:
    def demo_javascript_exec(self):
        driver = webdriver.Chrome()
        #driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
        driver.maximize_window()
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)

        time.sleep(3)
demojs = Demo_javascript()
demojs.demo_javascript_exec()