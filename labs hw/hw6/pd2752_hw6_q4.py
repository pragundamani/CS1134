from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(dll):
    res = DoublyLinkedList()
    curr = dll.header.next
    
    while curr is not dll.trailer:
        res.add_last(curr.data)
        curr = curr.next
    
    return res

def deep_copy_linked_list(dll):
    res = DoublyLinkedList()
    curr = dll.header.next
    
    while curr is not dll.trailer:
        if isinstance(curr.data, DoublyLinkedList):
            res.add_last(deep_copy_linked_list(curr.data))
        else:
            res.add_last(curr.data)
        curr = curr.next
    
    return res
