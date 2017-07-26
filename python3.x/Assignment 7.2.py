countx = 0
countline = 0
fname = input("open file name: ")
try:
	fhand = open(fname)
except:
	print ("file not found, ", fname)
for line in fhand:
	line = line.rstrip()
	if line.startswith ("X-DSPAM-Confiden"):
		stripped = line.strip("X-DSPAM-Confidence: ")
		countx = countx + float(stripped)
		countline = countline + 1
		fhand.close
print ("Average spam confidence:", countx / countline)

#desired output:
#Average spam confidence: 0.750718518519
