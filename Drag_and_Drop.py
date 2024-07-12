import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_drag_and_down:
    def demo_drag_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        drag_window = driver.find_element(By.ID, "draggable")
        drop_window = driver.find_element(By.ID, "droppable")
        time.sleep(3)
        Chains = ActionChains(driver)
        Chains.drag_and_drop(drag_window,drop_window).perform()
        time.sleep(3)
        
demo_drag = Demo_drag_and_down()
demo_drag.demo_drag_drop()