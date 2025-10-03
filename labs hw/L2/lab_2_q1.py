class Polynomial():
    def __init__(self,coefficients):
        self.data = coefficients
        
        if not coefficients:
            self.data = [0]

    def __add__(self,other):
        count = max(len(self.coefficients),len(other.coefficients))
        added = [0]*count

        for i in range(0,count):
        
            if i >= len(self.coefficients):
                added[i] = other.coefficients[i]
            elif i >= len(other.coefficients):
                added[i] = self.coefficients[i]
            else:
                added[i] = self.coefficients[i] + other.coefficients[i]
        
        return Polynomial(added)
    
    def __call__(self,param):
        result = 0
        
        for i in range(len(self.coefficients)):
            result += self.coefficients[i]*(param**i)
        return result
    
pol1 = Polynomial([3,7,0,-9,2])
pol2 = Polynomial([2,0,0,5,0,0,3])
pol3 = pol1+pol2
pol4 = Polynomial()

print(pol1(1))
print(pol2(1))
print(pol3(1))