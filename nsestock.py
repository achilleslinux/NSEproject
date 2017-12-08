#!/usr/bin/python/
from selenium import webdriver
import os
import time
import requests
from bs4 import BeautifulSoup
import urllib
import re
import cherrypy
import time


from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"
driver.get(url)
time.sleep(5)
htmlSource = driver.page_source
htmlSource = htmlSource.encode("utf-8")
soup = BeautifulSoup(htmlSource)
data = soup.find_all("table")
file = open("table.html","w")
for i in data:
    file.write(i.encode("utf-8"))

file.close()

file = open("table.html","r")
k=file.read()
print(k)

os.system("firefox final.html")
