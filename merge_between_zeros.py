from typing import Optional

"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        sm = 0
        while head:
            if head.val == 0:
                if sm > 0:
                    lst.append(sm)
                sm = 0
            sm += head.val
            head = head.next
        final_lst = ListNode(0)
        tmp = final_lst
        for i in lst:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return final_lst.next
