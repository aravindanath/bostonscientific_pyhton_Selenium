from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.icicibank.com/")
driver.fullscreen_window()
driver.find_element_by_id("modal-close").click()
time.sleep(3)
driver.find_element_by_class_name("ic-btn").click()
time.sleep(3)
driver.quit()



