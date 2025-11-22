import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)
#driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
#to wait for the dropdown options to display
time.sleep(2)
countries =driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

#to dynamically retrieve the value through the script
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"




