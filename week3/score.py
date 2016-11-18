score = raw_input("Enter Score: ")
digit =float(score)
if digit >1 or digit <0:
    print "out of range"
elif digit >=0.9:
    print "A"
elif digit >=0.8:
    print "B"
elif digit >=0.7:
    print "C"
elif digit >= 0.6:
    print "D"
else:
    print "F"