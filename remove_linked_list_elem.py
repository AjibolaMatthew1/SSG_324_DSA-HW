from typing import Optional

"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        # Step 2: Traverse the linked list, and remove any nodes that have value val
        while head:
            if head.val == val:
                # Skip over any nodes with value val
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        # Step 3: Return the head of the updated linked list (excluding the dummy node)
        return dummy.next
