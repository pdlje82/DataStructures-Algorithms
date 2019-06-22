### Calculate the floored square root of a number

The task is basically a binary search in an imaginary sorted array 
of integers: array = [i for i in range(0, number)]. This array is 
imaginary, because actually it is not used in the code. The code 
only operates on the array indices.

Another difference to an actual binary search is, that in the binary
search the search element is given externally, while in the sqrtinteger code
the search element is obtained after each array-split operation by 
squaring the middle element and comparing it to the number whose square
root is to be calculated.

As the search method remains the same as in binary search (split array ->
compare split value -> chose lower or upper split array -> repeat), the 
time and space complexity is the same as in binary search:

Time complexity: O(log n) \
Space complexity O(1)