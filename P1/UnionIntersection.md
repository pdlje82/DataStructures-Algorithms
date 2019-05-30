### Runtime Complexity for Union and Intersection using a Linked List as Datastructure

Traversing the linked lists is always O(n)

#### Union:
1. Go thru the first llist and write each element ONCE in the union list: O(n)
2. Go thru the second llist and add each element to union list, if not already there: O(n)

Overall complexity: O(n) + O(n) = O(n)

#### Inersection:
1. Check, if element is not in unionlist: O(n)
2. for each element in llist1 go thru llist 2 and check, if the element is also there: O(n^2)

Overall complexity: O(n^2) in the worst case