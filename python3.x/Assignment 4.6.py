def computepay(hours, rate):
    if hours<=40:
        result = hours * rate
        return result
    else:
        overtime = hours - 40
        result = overtime*(rate*1.50) + 40*rate
        return result
hours = input("enter hours: ")
rate = input ("enter rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print ("please enter a valid value.")
    quit()
pay = computepay(hours, rate)
print ("Pay", (str(pay)))
#desired output: Pay 498.75
