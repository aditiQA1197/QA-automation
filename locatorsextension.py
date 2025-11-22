import time

from selenium.webdriver.common.by import By

import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("aditigupta123@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("password")
driver.find_element(By.XPATH,"//form/div[3]/button").send_keys("password")
driver.find_element(By.XPATH,"//form/div[4]/button").click()
# or driver.find_element(By.XPATH,"//button[@type='submit']").click()

