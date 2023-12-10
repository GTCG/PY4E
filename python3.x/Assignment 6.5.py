text = "X-DSPAM-Confidence:    0.8475"
start = text.find(":")
startpos = text[start+1:]
number = (float(startpos))
print (number)
