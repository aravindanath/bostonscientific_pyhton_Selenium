from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.com/")
driver.find_element_by_css_selector("input[class$='gsfi']").send_keys("Iphone 13",Keys.ENTER)
time.sleep(2)
driver.close()




"""
 # id
 . class
 ^ starts with
 $ ends with
 * contains
"""