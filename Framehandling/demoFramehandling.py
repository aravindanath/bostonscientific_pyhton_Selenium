from LaunhBrowser import OpenChrome_UisngWM as oc
import time
from selenium.webdriver.common.action_chains import  ActionChains


oc.driver.get("https://the-internet.herokuapp.com/iframe")


oc.driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
ele = oc.driver.find_element_by_id("tinymce")
ele.clear()
time.sleep(2)
ele.send_keys("hello all!")

oc.driver.switch_to.default_content()

text = oc.driver.find_element_by_xpath("//h3").text

print(text)

time.sleep(2)

oc.driver.quit()