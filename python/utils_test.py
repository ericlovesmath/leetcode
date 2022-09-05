import utils


def linked_list_test():

    ll = utils.linkedList([1, 4, 2, 1])
    assert ll.val == 1
    assert ll.next.val == 4
    assert ll.next.next.val == 2
    assert ll.next.next.next.val == 1
    assert ll.next.next.next.next is None
    
    arr = utils.ll_to_arr(ll)
    assert arr == [1, 4, 2, 1]

    ll = utils.linkedList([])
    assert ll is None

    arr = utils.ll_to_arr(ll)
    assert arr == []

def bin_tree_test():
    arr = [1,10,4,3,None,7,9,12,8,6,None,None,2]
    tree = utils.binaryTree(arr)
    print(tree.val)
    print(tree.left.val, tree.right.val)
    print(tree.left.left.val, tree.right.left.val, tree.right.right.val)
    print(tree.left.left.left.val, tree.left.left.right.val, tree.right.left.left.val, tree.right.right.right.val)

    print(utils.bt_to_arr(tree))
    assert utils.bt_to_arr(tree) == arr

def main():
    linked_list_test()
    bin_tree_test()


main()
