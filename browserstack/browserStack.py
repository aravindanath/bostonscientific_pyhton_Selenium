from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials
    "browserstack.user": "joah_BklYP5",
    "browserstack.key": "8qyqmYGEYtmpzXXoyPvL",

    # Set URL of the application under test
    "app": "bs://2a885fbcad8883eb214b854a16e8a4fb9d36b5a6",

    # Specify device and os_version for testing
    "device": "Google Pixel 3",
    "os_version": "9.0",

    # Set other BrowserStack capabilities
    "project": "First Python project",
    "build": "browserstack-build-1",
    "name": "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

# If you have uploaded your app, write your test case here.

# Invoke driver.quit() after the test is done to indicate that the test is completed.
# driver.quit()
# driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
driver.implicitly_wait(20)
driver.find_element_by_xpath("//*[@resource-id='com.androidsample.generalstore:id/nameField']").send_keys("Arvind")

driver.find_element_by_xpath("//*[@text='Male']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@text,'Shop')]").click()
time.sleep(3)

driver.save_screenshot("demo.png")

driver.quit()
