#Assignment which belongs to chapter 13: Network programming
#In this assignment you will write a Python program that expands on 
#http://www.pythonlearn.com/code/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the 
#first name in the list, follow that link and repeat the process a number of times and report the last name you find. 

#This is a sample program Please paste the URL given in the assignment and follow the instructions when entering a number for count and position.

from urllib.request import urlopen
from bs4 import BeautifulSoup

count = int(input("Enter count: "))
position = int(input("Enter position: "))
number = 0

url = "http://py4e-data.dr-chuck.net/known_by_Dilraj.html"
print(url)

while number < count:
    number += 1
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    tags = soup("a")
    
    number2 = 0
    for tag in tags:
        number2 += 1
        if number2 == position:
            url = tag.get("href", None)
            print(url)
            break
