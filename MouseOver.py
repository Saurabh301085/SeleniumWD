from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Demo_mouse_hover():
    def demo_mouse_events(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        more_option = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        chains = ActionChains(driver)
        chains.move_to_element(more_option).perform()
        #more_option.click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        #xplore_item.click()
        time.sleep(3)

        driver.close()

demo_action_chain = Demo_mouse_hover()
demo_action_chain.demo_mouse_events()