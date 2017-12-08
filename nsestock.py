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
#driver = webdriver.Chrome('/usr/local/lib/python2.7/dist-packages/selenium/webdriver/remote/')
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"
#driver.get(url)
#time.sleep(5)
#htmlSource = driver.page_source

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
###
#print htmlSource

#r=requests.get(url)

#soup=BeautifulSoup(r.content,"lxml")
#print soup

#links=soup.find_all("div",{"class":"tabular_data_live_analysis"})

#for item in links:
#    print item.contents[1].find_all("")
#
