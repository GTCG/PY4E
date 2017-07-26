
#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message 
#and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")

    #input
    if num == "done" : break
    if len(num) == 0 : break

    try:
    	num = int(num)
    	if smallest is None or smallest > num :
    		smallest = num;
    		
    	if largest is None or largest < num :
    		largest = num;

    except Exception, e:
    	print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest

#desired output
#Invalid input
#Maximum is 7
#Minimum is 4

#Watch the Capitals!!
