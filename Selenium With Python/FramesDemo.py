from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


#   setting up chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)

#   go to the url
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")


#   switch to frame using id (we can also use frame name)
driver.switch_to.frame("mce_0_ifr")

#   handling frame
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I'am able to automate frames")

#   switch back to default browser scope
driver.switch_to.default_content()
print(driver.find_element(By. CSS_SELECTOR,"h3").text)