from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedVeggies =[]

#   click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#   collect all veggie names -> BrowserSortedveggieList ( A,B, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)
originalBrowserSortedList = browserSortedVeggies.copy()

#   Sort this BrowserSortedveggieList => newSortedList -> (A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
