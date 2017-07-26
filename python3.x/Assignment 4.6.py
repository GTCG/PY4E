def computepay(h,r):
	if h<=40:
		result = h*r
	else:
   	o = h-40    	
	result = o*(r*1.50) + 40*r
	return result

hours = input("enter hours:")
rate = input("enter rate:")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print ("please enter a valid value.")
    quit()
p = computepay(hours, rate)
print (p)

#desired output
#498.75
