import time

from LaunhBrowser import OpenChrome_UisngWM as oc
from selenium.webdriver.support.select import Select


oc.driver.get("https://demoqa.com/automation-practice-form")
oc.driver.maximize_window()
oc.driver.implicitly_wait(30)

oc.driver.find_element_by_id("firstName").send_keys("Arvind")

oc.driver.find_element_by_xpath("//label[text()='Male']").click()

oc.driver.find_element_by_id("dateOfBirthInput").click()

month = oc.driver.find_element_by_class_name("react-datepicker__month-select")

sel = Select(month)


sel.select_by_visible_text("May")

time.sleep(2)

year = oc.driver.find_element_by_class_name("react-datepicker__year-select")

sel =  Select(year)
sel.select_by_index(50)


oc.driver.find_element_by_xpath("//div[text()='22']").click()

cb = oc.driver.find_elements_by_xpath("//div[@class='custom-control custom-checkbox custom-control-inline']/label")

for c in cb:
    c.click()
time.sleep(2)

oc.driver.find_element_by_id("uploadPicture").send_keys("../testData.xlsx")

time.sleep(3)

oc.driver.quit()