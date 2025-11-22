#q5 answer pd2752
from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(node1, node2, result_list):
        if node1 is srt_lnk_lst1.trailer and node2 is srt_lnk_lst2.trailer:
            return
        
        if node1 is srt_lnk_lst1.trailer:
            result_list.add_last(node2.data)
            merge_sublists(node1, node2.next, result_list)
        elif node2 is srt_lnk_lst2.trailer:
            result_list.add_last(node1.data)
            merge_sublists(node1.next, node2, result_list)
        else:
            if node1.data <= node2.data:
                result_list.add_last(node1.data)
                merge_sublists(node1.next, node2, result_list)
            else:
                result_list.add_last(node2.data)
                merge_sublists(node1, node2.next, result_list)
    
    result = DoublyLinkedList()
    merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, result)
    return result