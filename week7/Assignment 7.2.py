#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute the average of those values 
#and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below 
#enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
countx = 0
countline = 0
fname = raw_input("open file name: ")
try:
	fhand = open(fname)
except:
	print "file not found, ", fname
for line in fhand:
	line = line.rstrip()
	if line.startswith ("X-DSPAM-Confiden"):
		stripped = line.strip("X-DSPAM-Confidence: ")
		countx = countx + float(stripped)
		countline = countline + 1
		fhand.close
print "Average spam confidence:", countx / countline

#desired output:
#Average spam confidence: 0.750718518519

		
		
