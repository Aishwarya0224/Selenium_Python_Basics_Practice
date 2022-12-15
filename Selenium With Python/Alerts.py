from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

name = "Aishwarya"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By. CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By. ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

# Checking that the name we entered is coming in the alert box
assert name in alertText

alert.accept()
#alert.dismiss()