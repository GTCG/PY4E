countx = 0
countline = 0
fname= input("enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print ("file not found, " , fname)
    quit()
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence: "):
        stripped = line.strip("X-DSPAM-Confidence: ")
        #print (stripped)
        countx = countx + float(stripped)
        countline = countline +1
fhand.close()
print ("Average spam confidence:" , countx/ countline)

#desired output:
#Average spam confidence: 0.750718518519
