# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Slow-Fast Cycle Detection
        if head is None or head.next is None:
            return None

        slow, fast = head.next, head.next.next
        while slow != fast:
            slow = slow.next
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     visited = set()
    #     while head != None:
    #         if head in visited:
    #             return head
    #         visited.add(head)
    #         head = head.next
    #     return None
