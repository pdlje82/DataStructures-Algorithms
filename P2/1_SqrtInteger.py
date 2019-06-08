'''
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor
value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))
'''


# use binary search / newton's method
# https://en.wikipedia.org/wiki/Bisection_method
# https://helloacm.com/binary-search-sqrt/

# def sqrt(number):
#     """
#     Calculate the floored square root of a number
#
#     Args:
#        number(int): Number to find the floored squared root
#     Returns:
#        int: Floored Square Root
#     """
#     low = 0
#     high = number
#
#     while low <= high:
#         mid = (low + high) // 2
#         #print('low {}, mid {}, high {}'.format(low, mid, high))
#         mid_squared = mid * mid
#         #print(mid_squared)
#         if mid_squared <= number:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low -1

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start_i = 0
    end_i = number

    while start_i <= end_i:
        split_i = (start_i + end_i) // 2
        squared = split_i * split_i
        if squared == number:
            print('1:', split_i)
            return split_i
        elif squared <= number:
            start_i = split_i + 1
        elif squared > number:
            end_i = split_i - 1
    return start_i - 1


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")