import time
import sys
import os 
import json

from selenium import webdriver
 

web1Info = open('/Users/eason/tools/config/web/web1.json') 
web1InfoData = json.load(web1Info)

driver = webdriver.Chrome("/Users/eason/Applications/chromedriver")


url = web1InfoData["url"] 
driver.get(url)

loginName = driver.find_element_by_id(web1InfoData["userNameKey"])
loginName.send_keys(web1InfoData["userName"])
loginPassword = driver.find_element_by_id(web1InfoData["passwordKey"])
loginPassword.send_keys(web1InfoData["password"])

clickButton = driver.find_element_by_css_selector(web1InfoData["buttonKey"])


clickButton.click()