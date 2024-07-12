import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_window_handler:
    def demo_multi_window_handler(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (upto Rs. 1,800) +Interest Free EMI on 3 and 6 months tenure']").click()
        all_handlers = driver.window_handles
        print(all_handlers)
        for handle in all_handlers:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//button[@id='subscribe']").click()
                time.sleep(4)
                driver.close()
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (upto Rs. 1,800) +Interest Free EMI on 3 and 6 months tenure']").click()
demowindow = Demo_window_handler()
demowindow.demo_multi_window_handler()