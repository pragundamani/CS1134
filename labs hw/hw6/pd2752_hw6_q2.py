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
        from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.digits = DoublyLinkedList()
        for char in num_str:
            if char.isdigit():
                self.digits.add_last(int(char))
    
    def __add__(self, other):
        result = Integer('')
        
        cursor1 = self.digits.trailer.prev
        cursor2 = other.digits.trailer.prev
        
        carry = 0
        
        while cursor1 is not self.digits.header or cursor2 is not other.digits.header or carry > 0:
            digit1 = cursor1.data if cursor1 is not self.digits.header else 0
            digit2 = cursor2.data if cursor2 is not other.digits.header else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            
            result.digits.add_first(digit)
            
            if cursor1 is not self.digits.header:
                cursor1 = cursor1.prev
            if cursor2 is not other.digits.header:
                cursor2 = cursor2.prev
        
        return result
    
    def __mul__(self, other):
        if self._is_zero() or other._is_zero():
            return Integer('0')
        
        result = Integer('0')
        
        cursor_other = other.digits.trailer.prev
        position = 0
        
        while cursor_other is not other.digits.header:
            multiplier_digit = cursor_other.data
            
            partial = Integer('')
            carry = 0
            
            cursor_self = self.digits.trailer.prev
            while cursor_self is not self.digits.header or carry > 0:
                self_digit = cursor_self.data if cursor_self is not self.digits.header else 0
                
                product = self_digit * multiplier_digit + carry
                carry = product // 10
                digit = product % 10
                
                partial.digits.add_first(digit)
                
                if cursor_self is not self.digits.header:
                    cursor_self = cursor_self.prev
            
            for _ in range(position):
                partial.digits.add_last(0)
            
            result = result + partial
            
            cursor_other = cursor_other.prev
            position += 1
        
        return result
    
    def _is_zero(self):
        cursor = self.digits.header.next
        while cursor is not self.digits.trailer:
            if cursor.data != 0:
                return False
            cursor = cursor.next
        return True
    
    def __repr__(self):
        if self.digits.is_empty():
            return '0'
        
        result = ''
        cursor = self.digits.header.next
        leading = True
        
        while cursor is not self.digits.trailer:
            if leading and cursor.data == 0:
                cursor = cursor.next
                continue
            leading = False
            result += str(cursor.data)
            cursor = cursor.next
        
        return result if result else '0'        
