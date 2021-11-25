from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/tables")

x = driver.find_element_by_xpath("//table[@id='table2']/tbody/tr/td[2][contains(text(),'Tim')]//preceding-sibling::td[1]").text

print(x)


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