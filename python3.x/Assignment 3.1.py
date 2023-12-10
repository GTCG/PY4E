hrs = input("Enter Hours:")
h = float(hrs)
rph = input("enter rate per hour:")
r = float(rph)
if h<=40:
    result = h*r
else:
    o = h-40
    result = o*(r*1.50) + 40*r

print (result)

#desired output
#498.75
