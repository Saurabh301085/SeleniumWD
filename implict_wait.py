import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_wait:
    def demo_implict_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.find_element(By.ID, "login-input").send_keys("7665445728")
        driver.find_element(By.XPATH, "//button[@id='login-continue-btn']").click()
        #ActionChains(driver).move_to_element(button).click(button).perform()
        driver.close()

impwait = Demo_wait()
impwait.demo_implict_wait()