from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.com/")
driver.find_element_by_partial_link_text("Imag").click()

driver.find_element_by_name("q").send_keys("bangalore",Keys.ENTER)

time.sleep(2)
driver.close()