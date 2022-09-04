from typing import Optional

from utils import ListNode, linkedList


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Link: https://leetcode.com/problems/merge-two-sorted-lists/
        Merge two sorted linked list such that it is sorted by the end.
        """

        dummy = head = ListNode(None)

        while True:
            if list1 is None:
                head.next = list2
                return dummy.next
            if list2 is None:
                head.next = list1
                return dummy.next

            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        # Space Complexity: O(1)
        # Time Complexity: O(m+n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.mergeTwoLists(
        linkedList([1, 2, 4]), linkedList([1, 3, 4])
    ) == linkedList([1, 1, 2, 3, 4, 4])

    assert sol.mergeTwoLists(linkedList([]), linkedList([])) == linkedList([])

    assert sol.mergeTwoLists(linkedList([]), linkedList([0])) == linkedList(
        [0]
    )
