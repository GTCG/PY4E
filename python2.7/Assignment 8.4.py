#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the 
#split() method. The program should build a list of words. For each word on each line check to see if the word is 
#already in the list and if not append it to the list. When the program completes, 
#sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
fh = open(fname)
words = []
for line in fh:
	line = line.split()
	for word in line:
		if word in words: continue
		else:
			words.append(word)
words.sort()
print words

#desired output
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 
#'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
