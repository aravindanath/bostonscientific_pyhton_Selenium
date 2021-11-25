from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

# path = "/Users/aravindanathdm/PycharmProjects/PythonSelenium/driver/chromedriver"

# driver = webdriver.Chrome(executable_path=path)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.wikipedia.org/")


lang = driver.find_elements(By.XPATH,"//select[@id='searchLanguage']/option")

print("Total lang count ",len(lang))
emptyList =[]
for x in lang:
   emptyList.append(x.text)

print("Unsorted Values ", emptyList)
emptyList.sort(reverse=False)
print("Sorted List", emptyList)

driver.quit()