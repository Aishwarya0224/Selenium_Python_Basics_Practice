from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("aishwarya@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#css selector
# Syntax: tagname[attribute='value'] -> example: input[name='name']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Aishwarya")

# css can be constructed taking any attribute of the lement wiht syntax
#idvalue
#.classname
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# handling Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
#dropdown.select_by_value


#xpath
# Syntax: //tagname[@attribute='value'] -> example: //input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
