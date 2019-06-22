### Rearrange Array Elements

Rearranging the array is required to eb done in O(log n) in the 
worst case, so mergesort is chosen. 
After the array is sorted, it is then traversed backwards, starting
from the end. The array elements are assigned in an alternating fashion
to each nummber, such that the last array element is the first digit of
the first number, the second last element of the array is the first digit of
the second number, the thirst last array element is the second digit
of teh first number and so on. This requires O(n) because the array
has to be traversed once. 

The overall time complexity is O(n log n)
Space complexity: O(n) because of merge sort
