from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


#   setting up chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#   for executing headless automation, ie: browser will not open at all.
chrome_options.add_argument("headless")
#   for handling certification errors in chrome browser - it will ignore all cerifocation and proceed to website.
chrome_options.add_argument("--ignore-certificate-errors")
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=driver_service)

#   go to the url
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#   handling javascript events using python - SCROLL
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#   taking simple screen shot and saving as file
driver.get_screenshot_as_file("scree.png")