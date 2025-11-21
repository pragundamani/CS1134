#q2 answer pd2752
from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self,num_str):
        self.data = DoublyLinkedList()
        for ch in num_str:
            self.data.add_last(int(ch))
    
    def __add__(self,other):
        carry = 0
        result = Integer("")
        node1 = self.data.trailer.prev
        node2 = other.data.trailer.prev
        while node1 is not self.data.header or node2 is not other.data.header:
            val1 = node1.data if node1 is not self.data.header else 0
            val2 = node2.data if node2 is not other.data.header else 0
            total = val1+val2+carry
            result.data.add_first(total%10)
            carry = total//10
            node1 = node1.prev if node1 is not self.data.header else None
            node2 = node2.prev if node2 is not other.data.header else None
        if carry>0:
            result.data.add_first(carry)
        return result

    def __repr__(self):
        return "".join(str(digit) for digit in self.data)
    
    def __mul__(self,other):
        pass