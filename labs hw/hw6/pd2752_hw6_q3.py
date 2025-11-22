from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        if not orig_str:
            return
        
        i = 0
        while i < len(orig_str):
            char = orig_str[i]
            count = 1
            while i + count < len(orig_str) and orig_str[i + count] == char:
                count += 1
            self.data.add_last((char, count))
            i += count
    
    def __add__(self, other):
        result = CompactString('')
        
        for char, count in self.data:
            result.data.add_last((char, count))
        
        if not self.data.is_empty() and not other.data.is_empty():
            last_self = self.data.trailer.prev.data
            first_other = other.data.header.next.data
            
            if last_self[0] == first_other[0]:
                result.data.trailer.prev.data = (last_self[0], last_self[1] + first_other[1])
                cursor = other.data.header.next.next
            else:
                cursor = other.data.header.next
        else:
            cursor = other.data.header.next
        
        while cursor is not other.data.trailer:
            result.data.add_last(cursor.data)
            cursor = cursor.next
        
        return result
    
    def __lt__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        count1_remaining = 0
        count2_remaining = 0
        
        while cursor1 is not self.data.trailer or cursor2 is not other.data.trailer or count1_remaining > 0 or count2_remaining > 0:
            if count1_remaining == 0:
                if cursor1 is not self.data.trailer:
                    char1, count1_remaining = cursor1.data
                    cursor1 = cursor1.next
                else:
                    return cursor2 is not other.data.trailer or count2_remaining > 0
            
            if count2_remaining == 0:
                if cursor2 is not other.data.trailer:
                    char2, count2_remaining = cursor2.data
                    cursor2 = cursor2.next
                else:
                    return False
            
            if char1 < char2:
                return True
            elif char1 > char2:
                return False
            else:
                min_count = min(count1_remaining, count2_remaining)
                count1_remaining -= min_count
                count2_remaining -= min_count
        
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
            result += char * count
        return result
    
    def __eq__(self, other):
        if len(self.data) != len(other.data):
            return False
        
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        
        while cursor1 is not self.data.trailer:
            if cursor1.data != cursor2.data:
                return False
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        
        return True