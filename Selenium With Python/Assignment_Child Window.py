import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#   setting up chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=driver_service)

#   go to the url
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#   clicking on the blinking text on parent window
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

#   handling child window
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])

#   grabbing text from red paragragh and closing the child window
textGrabbed = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
emailGrabed = textGrabbed.split(" ")[4]
print(emailGrabed)
driver.close()

#   moving back to parent window
driver.switch_to.window(windowOpened[0])

#   entering grabbed email id, password, clicking on signin button
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(emailGrabed)
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

#   explicit wait for error message
#   grab the error message and print it in o/p
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)