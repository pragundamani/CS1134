#q5 answer pd2752
from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(dll1, dll2):
    def merge_sublists(noda_1, noda_2, res_lst):
        if noda_1 is dll1.trailer and noda_2 is dll2.trailer:
            return
            
        if noda_1 is dll1.trailer:
            res_lst.add_last(noda_2.data)
            merge_sublists(noda_1, noda_2.next, res_lst)
        elif noda_2 is dll2.trailer:
            res_lst.add_last(noda_1.data)
            merge_sublists(noda_1.next, noda_2, res_lst)
        else:
            if noda_1.data <= noda_2.data:
                res_lst.add_last(noda_1.data)
                merge_sublists(noda_1.next, noda_2, res_lst)
            else:
                res_lst.add_last(noda_2.data)
                merge_sublists(noda_1, noda_2.next, res_lst)
    
    res = DoublyLinkedList()
    merge_sublists(dll1.header.next, dll2.header.next, res)
    return res
