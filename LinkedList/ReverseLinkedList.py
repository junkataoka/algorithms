"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

"""
Reasoning:
- We can reverse the linked list by using two pointers, prev and curr
- We can set prev to None and curr to head
- We can iterate through the linked list while curr is not None
- We can store the next node in a temp variable
- We can set the next node to prev
- We can set prev to curr
- We can set curr to temp
- We can return prev as the new head of the linked list

"""



 


