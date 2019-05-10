"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

d = {}
for e in calls:
    for number in e[0:2]:  # O(2)
        #print(number)
        if number not in d:
            d[number] = int(e[3])
        else:
            d[number] += int(e[3])

# for keys, values in d.items():
#     print(keys)
#     print(values)

max_caller = max(d, key=d.get)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_caller, d[max_caller]))

