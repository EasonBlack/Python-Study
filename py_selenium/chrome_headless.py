import time
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome("c:\Program Files (x86)\Google\chromedriver.exe",chrome_options=options)

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

time.sleep(5)

html_page = browser.page_source
soup = BeautifulSoup(html_page)
links = soup.select('.result .t a')
for link in links:
  print link.get_text()

browser.quit()
