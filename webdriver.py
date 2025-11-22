import time

import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service("/Users/aditigupta/Downloads/chromedriver‑142")
#driver=webdriver.Chrome(service=service_obj)
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
time.sleep(2)
print(driver.title)
print(driver.current_url)


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

