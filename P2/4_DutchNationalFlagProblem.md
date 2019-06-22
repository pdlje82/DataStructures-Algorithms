### Dutch National Flag Problem

This is solved by traversing the array with a "mid element"
 and swapping:
- the mid with the first element, if mid == 0
- the mid with the last element, if mid == 2

Time complexity: 
- get list element using its index: O(1)
- set list element using its index: O(1)
- traversing through the whole list: O(n)
Overall: O(n)

Space complexity: O(1) because only in-place operations used