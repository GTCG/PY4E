#this file is an assignment which belongs to chapter 11: Regular expressions
import re
count = 0
hand = open("numbers.txt")
lines = hand.read()
match = re.findall('[0-9]+',lines)
for i in match:
	number = int(i)
	count = count + number
print (count)
