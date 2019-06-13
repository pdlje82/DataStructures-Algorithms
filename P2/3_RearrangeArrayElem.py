"""
Rearrange Array Elements
Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers. You can
assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by
more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity
is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when
there are more than one possible answers, return any one.
"""


def re_array(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum

    Args:
       input_list(array): Input array to search
    Returns:
       output_array: array with the 2 numbers
    """
    input_list = mergesort(input_list)
    first = ""
    second = ""
    for i, e in enumerate(reversed(input_list)):
        print(i % 2)
        if i % 2 == 0:
            first += str(e)
        else:
            second += str(e)
    return [int(first), int(second)]


def test_function(test_case):
    if re_array(test_case[0]) == test_case[1]:
        print("Pass")
    else:
        print("Fail")


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


test_function([[5, 1, 4, 3, 2, 9, 6, 8, 7, 0], [97531, 86420]])
test_function([[3, 1, 0, 2], [31, 20]])
test_function([[9, 6, 7, 8, 5], [975, 86]])
