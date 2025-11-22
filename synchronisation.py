import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
#might need 2 secs to load
time.sleep(2)
items =  driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(items)
assert count > 0
