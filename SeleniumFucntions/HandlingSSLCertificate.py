from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
ops = ChromeOptions()
ops.add_argument("--ignore-certificate-errors")
driver = Chrome(ChromeDriverManager().install(),chrome_options=ops)

driver.get("https://www.cacert.org")
time.sleep(2)
driver.quit()
