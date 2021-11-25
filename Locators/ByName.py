from  LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.google.com")
oc.driver.find_element_by_name("q").send_keys("iphone 13 mini",Keys.ENTER)
time.sleep(3)
oc.driver.quit()

