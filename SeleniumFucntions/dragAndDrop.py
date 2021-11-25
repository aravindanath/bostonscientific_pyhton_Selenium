import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


oc.driver.get("http://demo.guru99.com/test/drag_drop.html")
oc.driver.maximize_window()
oc.driver.implicitly_wait(30)


src = oc.driver.find_element_by_xpath("//li[@id='fourth']/a")
dst = oc.driver.find_element_by_xpath("//ol[@id='amt7']/li")

act = ActionChains(oc.driver)
act.drag_and_drop(src,dst).perform()

time.sleep(3)

oc.driver.quit()