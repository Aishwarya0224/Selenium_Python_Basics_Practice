import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)

#  5 seconds is max time out.. 2 seconds (3 seconds save)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#  Validation of Search for items with "ber"
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

#  Special exception - due to find_elements to get [list of items] instead proceeding with []
time.sleep(3)

#  Validation of Product Selected (Result) & 
#  Validate Expected Product List Vs Actual Product List
#  Chaining of Web Elements
results = driver.find_elements(By. XPATH, "//div[@class='products']/div")
count = len(results)  #print(count)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click() 
assert expectedList == actualList
    
#  Validation of Cart Icon and Proceed to Checkout Button    
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By. XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#  Total Amount Validation
prices = driver.find_elements(By. CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text) # print(sum)
totalAmount = int(driver.find_element(By. CSS_SELECTOR, " .totAmt").text)
assert sum == totalAmount

#  Promo Code Validiation
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

#  Promo Apply Button Validiation
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#  Explicit Wait to Validate Promo Application
wait = WebDriverWait(driver,10)

#  Until Method expected_conditions to validate Promo Information Apprearance
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

#Total After Discount validation
discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount > discountedAmount