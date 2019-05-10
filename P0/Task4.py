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
for e in texts:  # save all text sending and receiving numbers in dict, O(n)
    # print(e)
    for number in e[0:2]:  # O(2)
        #print(number)
        if number not in d:
            d[number] = 's/r text'
            # print(number)
# print(len(d.keys()))

for e in calls:  # save all call receiving numbers in dict, O(n)
    # print(e)
    # for number in e[1]:
    #     print(number)
    if e[1] not in d:
        d[e[1]] = 'receive calls'
        #print(d[e[1]])
# print(len(d.keys()))

d1 = {}
for e in calls:  # outgoing calls, O(k)
    # for number in e[0]:
        # print(number)
        if e[0] not in d:  # if outgoing call was not receiving calls or sending/receiving texts
            d1[e[0]] = 'probably telemarketer'
# print(d1)
print("These numbers could be telemarketers:")
for key in sorted(d1.keys()):  # O(k log k)
    print(key)