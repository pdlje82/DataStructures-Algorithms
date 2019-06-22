### Search in a Rotated Sorted Array

This algorithm is also a modified version of binary search.
When dividing the array, one of the two halfes is sorted, which 
can be found out in O(1) by comparing the first and lat elements of
both split arrays. The code then checks, if the element is in the
sorted array (in O(1)) and chooses, in which split-array to continue 
recursively.

Time complexity: O(log n)
Space complexity: O(1)