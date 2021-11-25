from  LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.amazon.com")
oc.driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone 13 mini",Keys.ENTER)
time.sleep(3)
oc.driver.quit()

