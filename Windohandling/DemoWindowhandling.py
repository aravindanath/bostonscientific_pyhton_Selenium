from LaunhBrowser import OpenChrome_UisngWM as oc
import time
from selenium.webdriver.common.action_chains import  ActionChains


oc.driver.get("https://canarabank.com/")

loginh = oc.driver.find_element_by_xpath("//*[text()='LOGIN']")

act = ActionChains(oc.driver)
act.move_to_element(loginh).perform()

win1 = oc.driver.current_window_handle
print("Parent win id "+ win1)
print("Parent Page title "+oc.driver.title )
time.sleep(2)

oc.driver.find_element_by_xpath("//*[text()='Net Banking - Canara']").click()

wins = oc.driver.window_handles

oc.driver.switch_to.window(wins[1])

for w in wins:
    print(w)

print("Child Page title "+oc.driver.title )
time.sleep(3)

oc.driver.close()

oc.driver.switch_to.window(win1)

time.sleep(2)
print("Parent Page title "+oc.driver.title )



time.sleep(2)

oc.driver.quit()