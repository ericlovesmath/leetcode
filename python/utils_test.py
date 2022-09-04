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

def main():
    linked_list_test()


main()
