import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select

oc.driver.get("https://www.redbus.in/")
oc.driver.maximize_window()

oc.driver.find_element_by_xpath("//input[@id='src']").send_keys("bang")
time.sleep(2)

pickup =  oc.driver.find_elements_by_xpath("//ul[@class='autoFill homeSearch']/li")

for p in pickup:
    if p.text == "Yelahanka, Bangalore":
        p.click()
        break

time.sleep(2)


oc.driver.find_element_by_xpath("//input[@id='dest']").send_keys("hyd")
time.sleep(2)

drop =  oc.driver.find_elements_by_xpath("//ul[@class='autoFill homeSearch']/li")

for d in drop:
    if d.text == "LB Nagar, Hyderabad":
        d.click()
        break

time.sleep(2)

oc.driver.find_element_by_css_selector(".fl.icon-calendar_icon-new.icon-onward-calendar.icon").click()

date = oc.driver.find_elements_by_xpath("//table[@class='rb-monthTable first last']/tbody/tr/td")

for d in date:
    if d.text == "30":
        d.click()
        break
time.sleep(3)

oc.driver.find_element_by_id("search_btn").click()

time.sleep(5)

oc.driver.quit()