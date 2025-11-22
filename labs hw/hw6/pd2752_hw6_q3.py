#q3 answer pd2752
from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, og_str):
        self.data = DoublyLinkedList()
        if not og_str:
            return
        
        n = 0
        while n < len(og_str):
            char = og_str[n]
            count = 1
            while n+count < len(og_str) and og_str[n+count] == char:
                count += 1
            self.data.add_last((char, count))
            n += count
    
    def __add__(self, other):
        res = CompactString('')
        
        for char, count in self.data:
            res.data.add_last((char,count))
        
        if not self.data.is_empty() and not other.data.is_empty():
            self_end = self.data.trailer.prev.data
            oth_start = other.data.header.next.data
            
            if self_end[0] == oth_start[0]:
                res.data.trailer.prev.data = (self_end[0],self_end[1]+oth_start[1])
                curr = other.data.header.next.next
            else:
                curr = other.data.header.next
        else:
            curr = other.data.header.next
        
        while curr is not other.data.trailer:
            res.data.add_last(curr.data)
            curr = curr.next
        
        return res
    
    def __lt__(self, other):
        curr1 = self.data.header.next
        curr2 = other.data.header.next
        counter1 = 0
        counter2 = 0
        
        while curr1 is not self.data.trailer or curr2 is not other.data.trailer or counter1 > 0 or counter2 > 0:
            if counter1 == 0:
                if curr1 is not self.data.trailer:
                    char1, counter1 = curr1.data
                    curr1 = curr1.next
                else:
                    return curr2 is not other.data.trailer or counter2 > 0
            
            if counter2 == 0:
                if curr2 is not other.data.trailer:
                    char2, counter2 = curr2.data, curr2.data
                    curr2 = curr2.next
                else:
                    return False
            
            if char1<char2:
                return True
            elif char1>char2:
                return False
            else:
                min_count = min(counter1,counter2)
                counter1 -= min_count
                counter2 -= min_count
        
        return False
    
    def __le__(self, other):
        return self<other or self.__eq__(other)
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def __repr__(self):
        res = ''
        for char, count in self.data:
            res += char*count
        return res
    
    def __eq__(self,other):
        if len(self.data) != len(other.data):
            return False
        
        curr1 = self.data.header.next
        curr2 = other.data.header.next
        
        while curr1 is not self.data.trailer:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True
