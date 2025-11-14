from DoublyLinkedList import DoublyLinkedList
def move_to_last(self,node):
    node.prev.next = node.next
    node.next.prev = node.prev
    self.trailer.prev.next = node
    node.prev = self.trailer.prev
    self.trailer.prev = node
    node.next = self.trailer
    
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def alternating_parity(lst):
    def is_even(n):
        return n % 2 == 0
    def consisten(a,b):
        return (is_even(a) and not is_even(b)) or not (is_even(a) and not is_even(b))
    