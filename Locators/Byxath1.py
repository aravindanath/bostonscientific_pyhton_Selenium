from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.com/")
driver.find_element_by_xpath("//input[@name='q']").send_keys("Iphone 12",Keys.ENTER)
time.sleep(2)
driver.close()




"""
/html/body/div....

//tagname[@attribute = 'value']
//tagname[@attribute = 'value' and @attribute = 'value']
//tagname[@attribute = 'value' or @attribute = 'value']
contains
text
startswith
following
preceding
 
"""