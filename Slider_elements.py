from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class Demo_SLider():
    def demo_slider_event(self):
        driver = webdriver.Chrome()
        #driver.get("https://snapdeal.com/")
        driver.get("https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty")
        driver.maximize_window()
        # parent_handler = driver.current_window_handle
        # print(parent_handler)
        # men_wear = driver.find_element(By.XPATH, "//li[2]//a[1]//span[2]").click()
        # child_handles = driver.window_handles
        # print(child_handles)
        # time.sleep(6)
        # for handle in child_handles:
        #     if handle != parent_handler:
        #         driver.switch_to.window(handle)
        #         driver.find_element(By.XPATH, "//a[contains(@href,'https://www.snapdeal.com/products/mens-footwear-sports-shoes')]//span[contains(@class,'linkTest')][normalize-space()='Sports Shoes']").click()
        #         time.sleep(6)
        #         driver.close()
        #         break
        chains = ActionChains(driver)
        element1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        element2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")

        chains.drag_and_drop_by_offset(element1, 60, 0).perform()
        time.sleep(3)
        chains.drag_and_drop_by_offset(element2, -40, 0).perform()

demo_slider = Demo_SLider()
demo_slider.demo_slider_event()
