class UnsignedBinaryInteger:
    def _init_(self, num_str):
        self.num_str = num_str
    
    def decimal(self):
        decimal_value = 0
        for i, bit in enumerate(reversed(self.num_str)):
            if bit == '1':
                decimal_value += 2 ** i
        return decimal_value
    
    def _lt_(self, other):
        self_val = int(self.num_str, 2)
        other_val = int(other.num_str, 2)
        return self_val < other_val
    
    def _gt_(self, other):
        self_val = int(self.num_str, 2)
        other_val = int(other.num_str, 2)
        return self_val > other_val
    
    def _eq_(self, other):
        self_val = int(self.num_str, 2)
        other_val = int(other.num_str, 2)
        return self_val == other_val
    
    def is_twos_power(self):
        val = int(self.num_str, 2)
        return val > 0 and (val & (val - 1)) == 0
    
    def largest_twos_power(self):
        val = int(self.num_str, 2)
        if val <= 0:
            return 0
        
        power = 1 << (val.bit_length() - 1)
        return power
    
    def _repr_(self):
        return f"0b{self.num_str}"
    

#test = UnsignedBinaryInteger("1101")
#print(test.largest_twos_power())