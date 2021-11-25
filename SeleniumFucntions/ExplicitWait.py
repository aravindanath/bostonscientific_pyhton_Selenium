import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

oc.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
oc.driver.maximize_window()


oc.driver.find_element_by_xpath("//button[text()='Start']").click()

hello = oc.driver.find_element_by_xpath("//h4[text()='Hello World!']")

wait = WebDriverWait(oc.driver,30).until(ec.presence_of_element_located((By.XPATH,"//h4[text()='Hello World!']")))


print(hello.text)



time.sleep(3)

oc.driver.quit()