class Vector:                                                
    def __init__(self,d):  
        if isinstance(d,list):
            self.coords = d
        else:
            self.coords = [0]*d                             
    def __len__(self):
        return len(self.coords)                                                            
    def __getitem__(self, j):                              
        return self.coords[j]                              
    def __setitem__(self, j, val):                              
        self.coords[j] = val                              
    def __add__(self, other):                              
        if (len(self) != len(other)):                              
            raise ValueError("imensions must agree")                              
        result = Vector(len(self))                              
        for j in range(len(self)):                              
            result[j] = self[j] + other[j]                              
        return result                              
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return '<' + ', '.join(map(str, self.coords)) + '>'
    def __repr__(self):
        return str(self)


    def __sub__(self,other):
        if (len(self) != len(other)):                              
            raise ValueError("imensions must agree")                              
        # result = Vector(len(self))                              
        # for i in range(len(self)):                              
        #     result[i] = self[i] - other[i]
        return Vector([self[i]-other[i] for i in range(len(self))])
    def __neg__(self):
        return Vector([-j for j in self.coords])
    def __mul__(self,other):
        if isinstance(other,int):
            return Vector([k*other for k in self.coords])
        else:
            return sum([self[k]*other[k] for k in range(len(self))]) 
    def __rmul__(self,num):
        return self*num

# v1 = Vector(5)
# v1[1] = 10
# v1[-1] = 10
# print(v1)
# v2 = Vector([2, 4, 6, 8, 10])
# print(v2)
# u1 = v1 + v2
# print(u1)
# u2 = -v2
# print(u2)
# u3 = 3 * v2
# print(u3)
# u4 = v2 * 3
# print(u4)
# u5 = v1 * v2
# print(u5)