#Scraping Numbers from HTML using BeautifulSoup
#In this assignment you will write a Python program similar 
#to http://www.pythonlearn.com/code/urllink2.py. The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file. 

#Data Format

#The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

import urllib
import re
count = 0
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_283399.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("span")

for tag in tags:
	#print "contents:", tag.contents[1]
	stringnumber = tag.contents
	number= int(stringnumber[0-1])
	count = count+ number
print count

#Sample Execution

#$ python solution.py 
#Enter - http://python-data.dr-chuck.net/comments_42.html
#Count 50
#Sum 2...
