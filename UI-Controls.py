import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"///input[@type='checkbox'] ")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox .get_attribute("value") == "option2" :
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons =driver.find_elements(By.CSS_SELECTOR ,".radioButton")

radiobuttons[2].click()
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"hide-textbox").is_displayed()

name = "Aditi"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert =driver.switch_to.alert

alert_text =alert.text
print(alert_text)
assert name in alert_text
alert.accept()

