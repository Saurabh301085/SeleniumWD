import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demoscreenshot:
    def demo_screenshot_capture(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()

        screenshot_cap = driver.find_element(By.XPATH, "//input[@id='login-input']")
        screenshot_cap.send_keys("8058276982")
        #screenshotc.screenshot("C:\\Users\\Saurabh\\PycharmProjects\\SeleniumWD\\screenshots\\login.png")
        screenshot_cap1 = driver.find_element(By.XPATH, "//input[@id='login-input']")
        screenshot_cap1.click()
        time.sleep(3)
        #driver.get_screenshot_as_file("C:\\Users\\Saurabh\\PycharmProjects\\SeleniumWD\\screenshots\\error.png")
        driver.save_screenshot("C:\\Users\\Saurabh\\PycharmProjects\\SeleniumWD\\screenshots\\next.png")
        time.sleep(2)

        driver.quit()
captscrnshot = Demoscreenshot()
captscrnshot.demo_screenshot_capture()


