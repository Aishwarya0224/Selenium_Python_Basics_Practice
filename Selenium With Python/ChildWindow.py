from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By. LINK_TEXT, "Click Here").click()
# windows handles property will grab all the window names that is opened in a list format. it will store in the order the window is opened.
# 1st in [0]
# 2nd in [1] goes on..

windowOpened = driver.window_handles  #  handling parent window
print(driver.find_element(By. TAG_NAME, "h3").text)

driver.switch_to.window(windowOpened[1]) #  switching back to child window
print(driver.find_element(By. TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(windowOpened[0]) #  switching back to parent window
assert "Opening a new window" == driver.find_element(By. TAG_NAME, "h3").text