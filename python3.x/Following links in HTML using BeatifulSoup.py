#In this assignment you will write a Python program that expands on 
#http://www.pythonlearn.com/code/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the 
#first name in the list, follow that link and repeat the process a number of times and report the last name you find. 

#This is a sample program and I do not guarantee this program is the solution to the actual assignment, as it differs
#from time to time.


import urllib
from BeautifulSoup import *

count = int(input("enter count: "))
position= int(input("enter position: "))
number = 0
number2 = 0

url = "http://python-data.dr-chuck.net/known_by_Calah.html"
print (url)
html = urllib.urlopen(url).read()

while number<count:
	number = 0
	soup = BeautifulSoup(html)
	tags = soup("a")
	for tag in tags:
		number = number + 1
		while number2 < position:
			url = tag.get("href", None)
			print (url)
			html = urllib.urlopen(url).read()
			number2 +=1
