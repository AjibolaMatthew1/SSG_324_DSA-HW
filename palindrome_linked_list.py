from typing import Optional

"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
"""




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare the first and second half of the linked list
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
