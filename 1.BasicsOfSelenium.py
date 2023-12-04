from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://flutter.dev/")


print(driver.title)
#print(driver.page_source)
get_started = driver.find_element(By.LINK_TEXT,"Get started")
get_started.click()
search = driver.find_element(By.ID,"q")
search.click()
search.send_keys("Android")
search.send_keys(Keys.RETURN)
search_result= driver.find_element(By.CLASS_NAME,"gsc-expansionArea")
print(search_result.text)


    
    
