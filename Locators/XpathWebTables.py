from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.implicitly_wait(30)
driver.get("https://www.moneycontrol.com/markets/global-indices/")

comm =  ["GOLD","SILVER","COTTON"]

for x in comm:
    val = driver.find_element_by_xpath("//div[@id='comMCX']/div/table/tbody/tr/td/p/a[contains(text(),'"+x+"')]//following::td[1]").text
    print(x," ---> ",val)



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