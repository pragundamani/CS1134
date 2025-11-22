from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self,og):
        self.data = DoublyLinkedList()
        if not og:
            return
        
        n = 0
        while n < len(og):
            char = og[n]
            count = 1
            while n + count < len(og) and og[n+count] == char:
                count += 1
            self.data.add_last((char,count))
            n += count
    
    def __add__(self, other):
        result = CompactString('')
        
        for char, count in self.data:
            result.data.add_last((char, count))
        
        if not self.data.is_empty() and not other.data.is_empty():
            last_self = self.data.trailer.prev.data
            first_other = other.data.header.next.data
            
            if last_self[0] == first_other[0]:
                result.data.trailer.prev.data = (last_self[0], last_self[1] + first_other[1])
                pointer = other.data.header.next.next
            else:
                pointer = other.data.header.next
        else:
            pointer = other.data.header.next
        
        while pointer is not other.data.trailer:
            result.data.add_last(pointer.data)
            pointer = pointer.next
        
        return result
    
    def __lt__(self, other):
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next
        count1 = 0
        count2 = 0
        
        while pointer1 is not self.data.trailer or pointer2 is not other.data.trailer or count1 > 0 or count2 > 0:
            if count1 == 0:
                if pointer1 is not self.data.trailer:
                    char1, count1 = pointer1.data
                    pointer1 = pointer1.next
                else:
                    return pointer2 is not other.data.trailer or count2 > 0
            
            if count2 == 0:
                if pointer2 is not other.data.trailer:
                    char2, count2 = pointer2.data
                    pointer2 = pointer2.next
                else:
                    return False
            
            if char1 < char2:
                return True
            elif char1 > char2:
                return False
            else:
                minval = min(count1, count2)
                count1 -= minval
                count2 -= minval
        
        return False
    
    def __le__(self, other):
        return self < other or self.__eq__(other)
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def __repr__(self):
        result = ''
        for char, count in self.data:
            result += char*count
        return result
    
    def __eq__(self, other):
        if len(self.data) != len(other.data):
            return False
        
        pointer1 = self.data.header.next
        pointer2 = other.data.header.next
        
        while pointer1 is not self.data.trailer:
            if pointer1.data != pointer2.data:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return True
