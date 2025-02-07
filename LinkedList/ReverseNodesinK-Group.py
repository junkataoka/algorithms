"""
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:

Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:

Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
Constraints:

The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseGroup(head, k):

    def getKthNode(node, k):
        while k:
            if not node:
                return None
            node = node.next
            k -= 1
        return node

    def reverse(node, k):
            prev = None
            curr = node
            while k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k -= 1
            return prev

    dummy = ListNode(0)
    dummy.next = head
    groupPrev = dummy

    while True:
        kth = getKthNode(groupPrev, k)
        if not kth:
            break

        groupNext = kth.next
        original_head = groupPrev.next # Store the original head

        # Reverse the group
        newHead = reverse(original_head, k)

        # Connect the reversed group
        groupPrev.next = newHead
        original_head.next = groupNext

        # Move the groupPrev to the last node of the group
        groupPrev = original_head

    return dummy.next



