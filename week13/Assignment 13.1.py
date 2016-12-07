# Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
#comment counts from the XML data, compute the sum of the numbers in the file. 

#I do not guarantee this is the solution to the actual assignment, as this differs from time to time.

import json
import urllib
count = 0

url = "http://python-data.dr-chuck.net/comments_283400.json"
print "retrieving URL. Stand by."
uh = urllib.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print count

#Sample Execution

#$ python solution.py 
#Enter location: http://python-data.dr-chuck.net/comments_42.xml
#Retrieving http://python-data.dr-chuck.net/comments_42.xml
#Retrieved 4204 characters
#Count: 50
#Sum: 2...
