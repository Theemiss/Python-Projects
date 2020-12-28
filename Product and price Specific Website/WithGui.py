#!/usr/bin/python3
import tkinter as tk
from tkinter import Tk, Button, Frame, Entry, END
import time
from secretstorage import item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import os
f = open("results.csv","a")
def save(results,prices):
		for x,y in zip(results,prices):
			if x != None and y != None:
				f.write(x)
				f.write("\n")
				f.write(y)
				f.write("Rs")
				f.write("\n")

def close_window():
    root.destroy()
class App(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		button = tk.Button(text = "Quit", command = close_window)
		self.pack()
		button.pack()
		self.entrythingy = tk.Entry()
		self.entrythingy.pack()

		# Create the application variable.
		self.contents = tk.StringVar()
		# Set it to some value.
		self.contents.set("Sneakers")
		# Tell the entry widget to watch this variable.
		self.entrythingy["textvariable"] = self.contents

		# Define a callback for when the user hits return.
		# It prints the current value of the variable.
		button = tk.Button(text = "search", command = self.print_contents)
		button.pack()


	def print_contents(self):
		cwd = os.getcwd()
		path = cwd + "/chromedriver"
		print (path)
		DRIVER_PATH = path
		
		options = Options()
		options.headless = True
		options.add_argument("--window-size=1400,900")
		driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
		Url = "https://www.snapdeal.com/"
		driver.get(Url)
		products = driver.find_element_by_id("inputValEnter")
		products.send_keys(self.contents.get())
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
		save(results,prices)
		print("save done")
		driver.quit()
		print("closed")
root = tk.Tk()
myapp = App(root)
myapp.mainloop()
