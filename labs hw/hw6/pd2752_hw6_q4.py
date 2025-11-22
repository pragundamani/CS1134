from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    new_list = DoublyLinkedList()
    cursor = lnk_lst.header.next
    
    while cursor is not lnk_lst.trailer:
        new_list.add_last(cursor.data)
        cursor = cursor.next
    
    return new_list

def deep_copy_linked_list(lnk_lst):
    new_list = DoublyLinkedList()
    cursor = lnk_lst.header.next
    
    while cursor is not lnk_lst.trailer:
        if isinstance(cursor.data, DoublyLinkedList):
            new_list.add_last(deep_copy_linked_list(cursor.data))
        else:
            new_list.add_last(cursor.data)
        cursor = cursor.next
    
    return new_list