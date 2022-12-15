from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print("App title is ", driver.title)
print("App url is ", driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.quit()

#------------------------

# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/")
# print("App title is ", driver.title)
# print("App url is ", driver.current_url)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.forward()
# driver.quit()

#------------------------

# from selenium import webdriver
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/")
# print("App title is ", driver.title)
# print("App url is ", driver.current_url)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.forward()
# driver.quit()