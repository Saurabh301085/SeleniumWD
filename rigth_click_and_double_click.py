import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Demo_mouse_events:

    def demo_click_element(self):
        driver = webdriver.Chrome()
        #RIGTH Click Event
        # driver.get("https://www.w3schools.com/vue/tryit.php?filename=tryvue_modifiers_rightClick")
        # driver.maximize_window()
        # time.sleep(3)
        #
        # chain = ActionChains(driver)
        # driver.switch_to.frame("iframeResult_0")
        # click_element = driver.find_element(By.XPATH, "//div[@id='app']")
        # chain.context_click(click_element).perform()
        # time.sleep(3)

        #DOUBLE Click event
        driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_dblclick_trigger")
        driver.maximize_window()
        time.sleep(3)

        chains = ActionChains(driver)
        driver.switch_to.frame("iframeResult")
        click_element1 = driver.find_element(By.XPATH, "//button[normalize-space()='Trigger dblclick event for p element']")
        chains.double_click(click_element1)
        time.sleep(3)

demo = Demo_mouse_events()
demo.demo_click_element()
