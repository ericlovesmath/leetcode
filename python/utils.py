from typing import List, Optional


class ListNode:
    """Singly Linked List"""

    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __eq__(self, other) -> bool:
        return ll_to_arr(self) == ll_to_arr(other)


def ll_to_arr(node: Optional[ListNode]) -> List[int]:
    arr = []
    head = node
    while head is not None:
        arr.append(head.val)
        head = head.next
    return arr

def linkedList(arr: List[int]) -> Optional[ListNode]:
    dummy = head = ListNode()
    for num in arr:
        head.next = ListNode(num)
        head = head.next
    return dummy.next

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def binaryTree(arr):
	if not arr:
		return None
	N = len(arr)
	root = TreeNode(arr[0])
	queue = [root]
	i = 1
	while queue:
		cur = queue.pop(0)
		if i < N:
			if arr[i] is not None:
				cur.left = TreeNode(arr[i])
				queue.append(cur.left)
			i += 1
			if i < N:
				if arr[i] is not None:
					cur.right = TreeNode(arr[i])
					queue.append(cur.right)
				i += 1
	return root

def binaryTree2Arr(root):
	res = []
	queue = [root]
	while queue:
		cur = queue.pop(0)
		val = cur.val if cur else None
		res.append(val)
		if cur:
			queue.append(cur.left)
			queue.append(cur.right)
	while res and not res[-1]:
		res.pop()
	return res

