#!/usr/bin/python3
import tkinter as tk
import tkinter.font as font
import time
from secretstorage import item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import csv
import os
def close_window():
	root.destroy()
class App(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		myFont = font.Font(family='Courier', size=10, weight='bold')
		fileld = tk.Label(root, text="Number of Sentences")
		fileld.pack()
		self.entrythingy = tk.Entry()
		self.entrythingy.pack()
		# Create the application variable.
		self.contents = tk.StringVar()
		# Set it to some value.
		self.contents.set("1")
		# Tell the entry widget to watch this variable.
		self.entrythingy["textvariable"] = self.contents

		# Define a callback for when the user hits return.
		# It prints the current value of the variable.
		button1 = tk.Button(text = "Generate", command = self.generate,bg='#0052cc', fg='#000000')
		button1['font'] = myFont
		button1.pack()
		button2 = tk.Button(text = "Quit", command = close_window,bg='#0052cc', fg='#000000')
		button2['font'] = myFont
		self.pack()
		button2.pack(side=tk.BOTTOM)
	def generate(self):
		cwd = os.getcwd()
		path = cwd + "/chromedriver"
		DRIVER_PATH = path
		options = Options()
		options.headless = True
		options.add_argument("--window-size=1400,900")
		driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
		Url = "https://randomwordgenerator.com/"
		driver.get(Url)
		go_sentences = driver.find_element_by_xpath("/html/body/div[2]/nav/div/div[2]/ul/li[5]/a").click()
		time.sleep(5)
		number_of_sentence = driver.find_element_by_id("qty")
		number_of_sentence.send_keys(Keys.DELETE)
		number_of_sentence.send_keys(self.contents.get())
		number_of_sentence.send_keys(Keys.RETURN)
		senteence = driver.find_elements_by_xpath("//span[@class='support-sentence']")
		f = open('sentence.txt','a')
		for s in senteence:
			f.write(s.text)
			f.write("\n")
		f.close()
		driver.quit()

root = tk.Tk()
root.title("Random Sentence Generator")
root.geometry("220x200+300+300")
myapp = App(root)
myapp.mainloop()
