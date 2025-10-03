import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        if iter!=None:
            for i in iter:
                self.append(i)


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        # if (not (0 <= ind <= self.n - 1)):
        #     raise IndexError('invalid index')
        # return self.data_arr[ind] #(old)
        #new
        if ind<0:
            ind += self.n
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if ind<0:
            ind += self.n
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        return "[" + ", ".join(repr(self.data_arr[i]) for i in range(self.n)) + "]"
    
    def __add__(self,other):
        result = ArrayList()
        for i in range(self.n):
            result.append(self.data_arr[i])
        for i in range(other.n):
            result.append(other.data_arr[i])
        return result
    
    def __iadd__(self,other):
        for i in range(other.n):
            self.append(other.data_arr[i])
        return self
    
    def __mul__(self,k):
        result = ArrayList()
        for i in range(self.n):
            for j in range(k):
                result.append(self.data_arr[j])
        return result
    
    def __rmul__(self,k):
        return self * k
    
    def remove(self,val):
        for i in range(self.n):
            if self.data_arr[i] == val:
                for j in range(i,self.n-1):
                    self.data_arr[j] = self.data_arr[j+1]
                self.n -= 1
                return self
    
    def removeOdds(self):
        ind = 0
        for i in range(self.n):
            if self.data_arr[i]%2==0:
                self.data_arr[ind] = self.data_arr[i]
                ind += 1
        self.n = ind
        return self         

arr = ArrayList()
arr.append(1)
arr.append(2)
arr.append(3)
# print(arr)

arr2 = ArrayList()
arr2.append(4)
arr2.append(5)
arr2.append(6)
# print(arr + arr2)

# arr += arr2
# print(arr)

# print(arr[0],arr[-1])

# print(arr * 3)
# print(3 * arr)

# arr3 = ArrayList("python")
# print(arr3)

# arr.remove(2)
# print(arr)

# print(arr.removeOdds())