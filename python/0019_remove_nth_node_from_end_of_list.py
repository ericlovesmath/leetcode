from typing import Optional

from utils import ListNode, linkedList


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        Given the head of a linked list, remove the nth node from the
        end of the list and return its head.
        """

        # We will send a fast pointer `n` nodes ahead of a slow pointer
        # Then, we will simply remove the node at the slow pointer

        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head

        # Space Complexity: O(n)
        # Time Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()

    assert sol.removeNthFromEnd(linkedList([1, 2, 3, 4, 5]), 2) == linkedList(
        [1, 2, 3, 5]
    )
    assert sol.removeNthFromEnd(linkedList([1]), 1) == linkedList([])
    assert sol.removeNthFromEnd(linkedList([1, 2]), 1) == linkedList([1])
