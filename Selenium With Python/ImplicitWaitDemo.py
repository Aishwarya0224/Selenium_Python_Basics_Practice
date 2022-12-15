from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.implicitly_wait(5) 

# we should write immediately after declaring driver object using the browser

# this is global implicit wait. It wil be applied to all the lines of code. So whereever the object is not identified, it will wait untill that particular time.

# it will wait the max of 5 secs. but if the objct is displayed in lesser time further in the test without waiting for the time mentioned

# incase of sleep it will wait for the time mentioned no matter what - which is not effecient

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# here dint remove sleep becoz 
# 1. find_elements will not get caught for implicit wait - it retuns the list of web elements. even if no web elements are there it will still return an empty list [] which is valid.

# selenium will consider the [] as list received and will continue further
# but technically items are stil not loaded.  since the list is written immediately [] - it will accept that and continue, will end error. Selenium will not know  that the list should be items - it will see for return type and continue 

# but if we wait 2 mins we will get actual / desired list. this is the only exception

results = driver.find_elements(By. XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By. XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
