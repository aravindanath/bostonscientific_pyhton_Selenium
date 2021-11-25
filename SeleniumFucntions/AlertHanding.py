import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select


oc.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
oc.driver.maximize_window()
oc.driver.implicitly_wait(30)



oc.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()

alt = oc.driver.switch_to.alert
alt.accept()

time.sleep(1)

oc.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
alt = oc.driver.switch_to.alert
alt.dismiss()
time.sleep(1)

oc.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
alt = oc.driver.switch_to.alert
alt.send_keys("Hello all")
alt.accept()

time.sleep(1)

result = oc.driver.find_element_by_id("result").text
print("result "+ result)


time.sleep(3)

oc.driver.quit()