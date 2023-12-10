name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
d = dict()

for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        d[hour] = d.get(hour, 0) + 1

# Sort the dictionary by keys
sorted_d = dict(sorted(d.items()))

# Print the sorted dictionary
for key, val in sorted_d.items():
    print(key, val)
