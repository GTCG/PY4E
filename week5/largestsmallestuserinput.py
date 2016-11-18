largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	try:
		num = int(num)
	except:
		print "Invalid input"
	if num <= largest:
		largest = num
	if num >= smallest:
		smallest = num
	if num == "done" : break
	print num

print "Maximum is", largest
print "Minimum is", smallest