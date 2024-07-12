import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DemoAutosuggest:
    def demo_auto_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        #driver.refresh()
        # Autosuggestion method
        # this way to select the value using keys enter
        departure_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departure_city.click()
        time.sleep(3)
        departure_city.send_keys("New Delhi")
        time.sleep(3)
        departure_city.send_keys(Keys.ENTER)
        time.sleep(5)
        # this way is used when you want to suggestion from list and select from it
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(3)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for results in search_results:
            if "New York (JFK)"in results.text:
                results.click()
                time.sleep(3)
                break

        # Calendar Selection (Hardcoded method)
        departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        departure_date.click()
        time.sleep(3)
        # driver.find_element(By.XPATH, "//td[@id='31/07/2024']").click()
        # time.sleep(3)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for dates in all_dates:
            if dates.get_attribute("data-date") == "30/10/2024":
                dates.click()
                time.sleep(3)
                break
        driver.quit()
dauto = DemoAutosuggest()
dauto.demo_auto_dropdown()


