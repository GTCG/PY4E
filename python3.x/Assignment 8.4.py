fname = input("Enter file name: ")
fh = open(fname)
words = []
for line in fh:
	line = line.split()
	for word in line:
		if word in words: continue
		else:
			words.append(word)
words.sort()
print (words)
