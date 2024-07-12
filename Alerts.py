import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_popup_windows:
    def demo_alerts(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()

        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # to accept the alert
        #driver.switch_to.alert.accept()
        # to reject the alert
        #driver.switch_to.alert.dismiss()
        #to accept with the text
        driver.switch_to.alert.send_keys("I am Nobody")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.quit()


alertwin = Demo_popup_windows()
alertwin.demo_alerts()
