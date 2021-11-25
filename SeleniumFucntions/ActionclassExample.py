import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


oc.driver.get("https://www.myntra.com/")
oc.driver.maximize_window()
oc.driver.implicitly_wait(30)

women = oc.driver.find_element_by_xpath("(//a[text()='Women'])[1]")
act = ActionChains(oc.driver)
act.move_to_element(women).perform()
time.sleep(2)

jacket = oc.driver.find_element_by_xpath("(//a[text()='Jackets & Coats'])[1]")
act = ActionChains(oc.driver)
act.click(jacket).perform()

time.sleep(3)

oc.driver.quit()