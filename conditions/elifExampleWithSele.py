from selenium.webdriver import Chrome,Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser = "Firefox"
global driver
if browser.lower() == "chrome":
    driver = Chrome(ChromeDriverManager().install())
elif browser.lower() == "Firefox":
    driver = Firefox(GeckoDriverManager().install())
else:
    print("Enter either chrome or firefox")

driver.get("https://www.google.com")