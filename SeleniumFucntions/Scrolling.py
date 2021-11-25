from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(1)

backtoTop =  driver.find_element_by_xpath("//span[contains(text(),'Back to top')]")

driver.execute_script("arguments[0].scrollIntoView();",backtoTop)

time.sleep(2)
backtoTop.click()
time.sleep(2)
driver.quit()
