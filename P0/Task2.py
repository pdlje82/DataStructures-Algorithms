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

call_durations = [row[3] for row in calls]  # O(n)
call_durations = list(map(int, call_durations))
mymax = max(call_durations)  # O(n)
max_index = call_durations.index(mymax)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(calls[max_index][0], mymax))
