import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demo_Explicit:
    def demo_explicit_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        #driver.refresh()
        # Autosuggestion method
        # this way to select the value using keys enter
        departure_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departure_city.click()
        #time.sleep(3)
        departure_city.send_keys("New Delhi")
        #time.sleep(3)
        departure_city.send_keys(Keys.ENTER)
        #time.sleep(5)
        # this way is used when you want to suggestion from list and select from it
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        #time.sleep(3)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                #time.sleep(3)
                break

        driver.get_screenshot_as_file("C:\\Users\\Saurabh\\PycharmProjects\\SeleniumWD\\screenshots\\yatralogin.png")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # Calendar Selection (Hardcoded method)
        #departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        #departure_date.click()
        #time.sleep(3)
        # driver.find_element(By.XPATH, "//td[@id='31/07/2024']").click()
        # time.sleep(3)
        all_dates = (wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).
                     find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))
        #all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for dates in all_dates:
            if dates.get_attribute("data-date") == "30/10/2024":
                dates.click()
                #time.sleep(3)
                driver.quit()
                break
        driver.find_element(By.ID, "BE_flight_flsearch_btn").click()
        #time.sleep(5)


waits = Demo_Explicit()
waits.demo_explicit_wait()
