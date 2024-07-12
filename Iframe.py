import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_iframe:
    def demo_window_frame(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@class='user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login']")
        driver.close()

demo_test = Demo_iframe()
demo_test.demo_window_frame()