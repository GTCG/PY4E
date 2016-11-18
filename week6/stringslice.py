str = "X-DSPAM-Confidence:  0.8475"
location1 = str.find(" ")
location2 = str.find("5")
number = str[location1:location2+1]
num = float(number.strip())
print num