#!/usr/bin/python3
import time
from secretstorage import item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import itertools
import os

cwd = os.getcwd()
path = cwd + "/chromedriver"
DRIVER_PATH = path
options = Options()
options.headless = True
options.add_argument("--window-size=1400,900")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
Url = "https://www.livescore.com/en/"
driver.get(Url)
time.sleep(5)

cookie = driver.find_element_by_id("onetrust-accept-btn-handler")
cookie.click()
#today
ligue = driver.find_elements_by_xpath("//span[@class='stage']")
teams = driver.find_elements_by_xpath("//span[@class='team-name']")
score_home = driver.find_elements_by_xpath("//span[@class='score__home']")
score__away = driver.find_elements_by_xpath("//span[@class='score__away']")
Time = driver.find_elements_by_xpath("//span[@class='MatchRowTime__Time-sc-1a2nnc7-1 lntdxq']")
with open('score.csv', mode='w') as employee_file:
	employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	employee_writer.writerow(["Time","Team A","Score Home","Score Away","Team B"])
	
	for t,x,h,a,y in itertools.zip_longest(Time,teams[0::2],score_home,score__away,teams[1::2]):
		if t is None:
			employee_writer.writerow(["",x.text,h.text,a.text,y.text])
		elif  h.text == "?":
			employee_writer.writerow(["",x.text,"","",y.text])
		else:
			employee_writer.writerow([t.text,x.text,h.text,a.text,y.text])
		


driver.quit()