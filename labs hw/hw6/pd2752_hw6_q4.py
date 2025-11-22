from DoublyLinkedList import DoublyLinkedList
import copy

def copy_linked_list(dll):
    res = DoublyLinkedList()
    curr = dll.header.next
    while curr is not dll.trailer:
        res.add_last(copy.copy(curr.data))
        curr = curr.next
    return res

def deep_copy_linked_list(dll):
    res = DoublyLinkedList()
    curr = dll.header.next
    while curr is not dll.trailer:
        res.add_last(copy.deepcopy(curr.data))
        curr = curr.next
    return res