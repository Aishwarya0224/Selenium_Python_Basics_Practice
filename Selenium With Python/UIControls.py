from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.maximize_window()

# handling Checkbox
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        # print(checkbox.is_selected()) - to know if we selected that check box
        assert checkbox.is_selected()
        break
    
# handling radio button
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()