from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.indusind.com/in/en/personal.html")

try:
    driver.find_element_by_xpath("(//a[@class='close'])[1]").click()
except:
    print("Notification is disabled")

driver.find_element_by_link_text("About Us").click()

time.sleep(3)
driver.quit()

