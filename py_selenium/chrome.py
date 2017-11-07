import time
from selenium import webdriver

browser = webdriver.Chrome("c:\Program Files (x86)\Google\chromedriver.exe")
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
# browser.quit()
