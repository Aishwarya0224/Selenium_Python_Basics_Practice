from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# right click on Top
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()                                   