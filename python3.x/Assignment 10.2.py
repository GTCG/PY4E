name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
t = list()
d = dict()
for line in handle:
    if line.startswith("From "):
		line = line.rstrip()
		words = line.split()
		time = words[5]
		hour = time[0:2]
		d[hour] = d.get(hour,0) +1
#for key, val in d.items():
t = d.items()
t.sort()
for key, val in t:
    print (key, val)
