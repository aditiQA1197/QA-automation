import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


expected_list = ['Cucumber - 1 Kg' ,'Raspberry - 1/4 Kg' ,'Strawberry - 1/4 Kg']
actual_list=[]


service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
#might need 2 secs to load
time.sleep(2)
items =  driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(items)
assert count > 0
#chaining the web elements
#each item in items list finds the corresponding button three times and clicks
#the loop iterates three times and clicks the button three times
for item in items :
    actual_list.append(item.find_element(By.XPATH,"h4").text)
    item.find_element(By.XPATH,"div/button").click()

assert (actual_list) == (expected_list)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices :
    sum = sum+ int(price.text)

print(sum)
totalsum = int(driver.find_element(By.CSS_SELECTOR ,".totAmt").text)
assert sum == totalsum


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

discounted_amount= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalsum > discounted_amount

