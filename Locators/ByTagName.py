from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.com/")

links = driver.find_elements_by_tag_name("a")

print("Total no of links ",len(links))

for x in links:
    print(x.text, " ---> ", x.get_attribute("href"))

time.sleep(2)
driver.close()