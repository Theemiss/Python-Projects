#!/usr/bin/python3
import time
from secretstorage import item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import os
cwd = os.getcwd()
path = cwd + "/chromedriver"
DRIVER_PATH = path
options = Options()
options.headless = True
options.add_argument("--window-size=1400,900")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
Url = "https://www.snapdeal.com/"
driver.get(Url)
products = driver.find_element_by_id("inputValEnter")
userinput = input("Enter keyword : ")
products.send_keys(userinput)
products.send_keys(Keys.RETURN)
time.sleep(5)
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:	
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)	
	results = [item.get_attribute("title")for item in driver.find_elements_by_class_name("product-title")]
	prices = [item.get_attribute("data-price")for item in driver.find_elements_by_class_name("product-price")]
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	last_height = new_height

with open('results.csv', mode='w') as employee_file:
	employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)	
	employee_writer.writerow(['Product','Price'])
	for x,y in zip(results,prices):
		employee_writer.writerow([x,y])

driver.quit()
