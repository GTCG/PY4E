
#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

str = "X-DSPAM-Confidence:  0.8475"
location1 = str.find(" ")
location2 = str.find("5")
number = str[location1:location2+1]
num = float(number.strip())
print num

#desired output:
# 0.8475
