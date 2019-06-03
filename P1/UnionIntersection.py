"""
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is
the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B,
is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection,
respectively. Once you have completed the problem you will create your own test cases and perform your own run time
analysis on the code.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):  # prints self value if instance is called
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def is_in_list(self, value):
        if self.head is None:
            return False
        node1 = self.head
        while node1.next:
            if node1.value == value:
                return True
            node1 = node1.next
        if node1.value == value:
            return True
        return False


def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size() == 0 or llist_2.size() == 0:
        print('Cannot execute union with empty list')
        return
    union_list = LinkedList()
    for e in llist_1, llist_2:
        node = e.head
        while node.next:
            if not union_list.is_in_list(node.value):
                union_list.append(node.value)
            node = node.next
        if not union_list.is_in_list(node.value):
            union_list.append(node.value)
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.size() == 0 or llist_2.size() == 0:
        print('Cannot execute intersection with empty list')
        return
    intersect_list = LinkedList()
    node = llist_1.head
    while node.next:
        if not intersect_list.is_in_list(node.value):
            if llist_2.is_in_list(node.value):
                intersect_list.append(node.value)
        node = node.next
    if not intersect_list.is_in_list(node.value):
        if llist_2.is_in_list(node.value):
            intersect_list.append(node.value)
    return intersect_list


# Test case 1
print('\nTest Case 1_________________________________________________________________')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1, '\n', linked_list_2)

print('union: ', union(linked_list_1, linked_list_2))
print('intersection: ', intersection(linked_list_1, linked_list_2))

# Test case 2
print('\nTest Case 2_________________________________________________________________')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1, 1, 1, 8, 1, 21, 1, 1, 1, 21]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3, '\n', linked_list_4)

print('union: ', union(linked_list_3, linked_list_4))
print('intersection: ', intersection(linked_list_3, linked_list_4))

# Test case 3
print('\nTest Case 3_________________________________________________________________')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3, '\n', linked_list_4)

print('union: ', union(linked_list_3, linked_list_4))
print('intersection: ', intersection(linked_list_3, linked_list_4))