from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = curr = ListNode(None, head)
        while (curr.next != None and curr.next.next != None):
            fst, snd = curr.next, curr.next.next
            curr.next = snd
            fst.next = snd.next
            snd.next = fst
            curr = curr.next.next
        return sentinel.next
