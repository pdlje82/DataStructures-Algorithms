"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

d = {}
for e in texts:  # save all text sending and receiving numbers in dict
    # print(e)
    for number in e[0:2]:
        if number not in d:
            d[number] = 's/r text'
            # print(number)
# print(len(d.keys()))

for e in calls:  # save all call receiving numbers in dict
    for number in e[1]:
        if number not in d:
            d[number] = 'receive calls'
# print(len(d.keys()))

d1 = {}
for e in calls:  # outgoing calls
    for number in e[0]:
        if number not in d:  # if outgoing call was not receiving calls or sending/receiving texts
            d1[number] = 'probably telemarketer'
# print(d1)
print("These numbers could be telemarketers:")
for key in sorted(d1.keys()):
    print(key)