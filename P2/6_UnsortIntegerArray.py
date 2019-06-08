"""
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

# It's just finding the min and max in O(n) time, but without using Python's inbuilt functions.

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = ints[0]
    min = ints[0]
    for e in ints[1:]:
        if e > max:
            max = e
        elif e < min:
            min = e
    return (min, max)


## Example Test Case of Ten Integers
import random


# Test Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 2
l = [i for i in range(0, 10000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9999) == get_min_max(l)) else "Fail")

# Test Case 3
l = [i for i in range(-10000, 10000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-10000, 9999) == get_min_max(l)) else "Fail")
