#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers. 

#Data Format

#The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

#Why should you learn to write programs? 7746
#12 1929 8827
#Writing programs (or programming) is a very creative 
#7 and rewarding activity.  You can write programs for 
#many reasons, ranging from making your living to solving
#8837 a difficult data analysis problem to having fun to helping 128
#someone else solve a problem.  This book assumes that 
#everyone needs to know how to program ...

#This is a sample program and I do not guarantee it is the solution to the actual assignment, as this differs often.
#I have included a sample file to test the program.

import re
count = 0
hand = open("numbers.txt")
lines = hand.read()
match = re.findall('[0-9]+',lines)
for i in match:
	number = int(i)
	count = count + number
print count
