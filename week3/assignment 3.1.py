hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("enter rate per hour:")
r = float(rph)
if h<=40:
	result = h*r
else:
    o = h-40
    result = o*(r*1.50) + 40*r

print result
