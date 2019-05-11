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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

d = {}
for e in calls:
    if '080' in e[0]:
        if e[1] not in d:
            d[e[1]] = True  # O(n)

d1 = {}
for key in d:
    if key[0] is '7' or key[0] is '8' or key[0] is '9':
        if key[0:4] not in d1:
            d1[key[0:4]] = 'mobile'  # [0:4] would be more correct, but [0:5] saves also 'space' character
    elif key[0:3] is '140':
        if '140' not in d1:
            d1['140'] = 'telemarketing'
    elif key[0] == '(':
        if key[key.find("("):key.find(")")+1] not in d1:
            d1[key[key.find("("):key.find(")")+1]] = 'landline'  # O(k)

print("The numbers called by people in Bangalore have codes:")
for key in sorted(d1.keys()):  # O(k log k)
    print(key)


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
callers = 0
receivers = 0
for e in calls:
    if '080' in e[0]:
        callers += 1
        if '080' in e[1]:
            receivers += 1  # O(n)

print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(100 / callers * receivers))