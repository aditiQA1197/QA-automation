import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)
#driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID , Xpath , CSS selector , ClassName , name , linkText
driver.find_element(By.CSS_SELECTOR ,"input[name='name']").send_keys("Aditi Gupta")
driver.find_element(By.NAME, "email").send_keys("aditi.gupta119211@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#static dropdown
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Male")

driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(3)

# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
#assert "Success" in message

assert "Success123" in message
driver.find_element(By.XPATH ,"(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH ,"(//input[@type='text'])[3]").clear()


