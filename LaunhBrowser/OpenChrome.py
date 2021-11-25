from selenium.webdriver import Chrome

path = "/Users/aravindanathdm/PycharmProjects/PythonSelenium/driver/chromedriver"

driver = Chrome(executable_path=path)

driver.get("https://www.google.com")


