input =input("How many degrees Celsius?")
try:    
  C = float(input)
except:
  print ("please enter a valid number! No "," allowed")
F =  C * 1.8 + 32
print (C, "degrees Celsius is equal to", F, "degrees Fahrenheit")
