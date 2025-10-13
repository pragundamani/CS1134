# import ctypes
# def make_array(n):
#     return (n * ctypes.py_object)()

# class ArrayList:
#     # Q1 (g) - Modified constructor to accept iterable collections
#     def __init__(self, iterable=None):
#         self.data_arr = make_array(1)
#         self.capacity = 1
#         self.n = 0
#         if iterable is not None:
#             for elem in iterable:
#                 self.append(elem)


#     def __len__(self):
#         return self.n

    
#     def append(self, val):
#         if (self.n == self.capacity):
#             self.resize(2 * self.capacity)
#         self.data_arr[self.n] = val
#         self.n += 1


#     def resize(self, new_size):
#         new_array = make_array(new_size)
#         for i in range(self.n):
#             new_array[i] = self.data_arr[i]
#         self.data_arr = new_array
#         self.capacity = new_size

#     def __iter__(self):
#         for i in range(len(self)):
#             yield self.data_arr[i]  


#     def extend(self, iter_collection):
#         for elem in iter_collection:
#             self.append(elem)

#     # Q1 (a) - Implement __repr__ method for ArrayList display
#     def __repr__(self):
#         result = "["
#         for i in range(self.n):
#             if i > 0:
#                 result += ", "
#             result += repr(self.data_arr[i])
#         result += "]"
#         return result

#     # Q1 (b) - Implement __add__ method for concatenation (arr1 + arr2)
#     def __add__(self, other):
#         result = ArrayList()
#         for i in range(self.n):
#             result.append(self.data_arr[i])
#         for i in range(other.n):
#             result.append(other.data_arr[i])
#         return result

#     # Q1 (c) - Implement __iadd__ method for in-place concatenation (arr1 += arr2)
#     def __iadd__(self, other):
#         for i in range(other.n):
#             self.append(other.data_arr[i])
#         return self

#     # Q1 (d) - Modified __getitem__ to support negative indices
#     def __getitem__(self, ind):
#         if ind < 0:
#             ind = self.n + ind
#         if (not (0 <= ind <= self.n - 1)):
#             raise IndexError('invalid index')
#         return self.data_arr[ind]


#     # Q1 (d) - Modified __setitem__ to support negative indices
#     def __setitem__(self, ind, val):
#         if ind < 0:
#             ind = self.n + ind
#         if (not (0 <= ind <= self.n - 1)):
#             raise IndexError('invalid index')
#         self.data_arr[ind] = val

#     # Q1 (e) - Implement __mul__ method for repetition (arr * k)
#     def __mul__(self, k):
#         result = ArrayList()
#         for _ in range(k):
#             for i in range(self.n):
#                 result.append(self.data_arr[i])
#         return result


#     # Q1 (f) - Implement __rmul__ method for reverse multiplication (k * arr)
#     def __rmul__(self, k):
#         return self.__mul__(k)


#     # Q1 (h) - Implement remove() method to remove first instance of val
#     def remove(self, val):
#         for i in range(self.n):
#             if self.data_arr[i] == val:
#                 for j in range(i, self.n - 1):
#                     self.data_arr[j] = self.data_arr[j + 1]
#                 self.n -= 1
#                 return


#     # Q1 (i) - Implement removeOdds() method to remove all odd values in-place
#     def removeOdds(self):
#         write_index = 0
#         for read_index in range(self.n):
#             if self.data_arr[read_index] % 2 == 0:
#                 self.data_arr[write_index] = self.data_arr[read_index]
#                 write_index += 1
#         self.n = write_index


#     # Q2 (a)
#     def insert(self, index, val):
#         if index < 0:
#             index = self.n + index
#             if index < 0:
#                 raise IndexError('invalid index')
#         if index > self.n or index < 0:
#             raise IndexError('invalid index')
#         if self.n == self.capacity:
#             self.resize(2 * self.capacity)
#         for i in range(self.n, index, -1):
#             self.data_arr[i] = self.data_arr[i - 1]
#         self.data_arr[index] = val
#         self.n += 1
    
#     # Q2 (b)
#     # def pop(self):
#     #     if self.n == 0:
#     #         raise IndexError('pop from empty list')
#     #     last_elem = self.data_arr[self.n - 1]
#     #     self.data_arr[self.n - 1] = None
#     #     self.n -= 1
#     #     if self.n < self.capacity // 4 and self.capacity > 1:
#     #         self.resize(self.capacity // 2)
#     #     return last_elem
    
#     # Q2 (d)
#     def pop(self, index=None):
#         if index is None:
#             if self.n == 0:
#                 raise IndexError('pop from empty list')
#             last_elem = self.data_arr[self.n - 1]
#             self.data_arr[self.n - 1] = None
#             self.n -= 1
#             if self.n < self.capacity // 4 and self.capacity > 1:
#                 self.resize(self.capacity // 2)
#             return last_elem
#         else:
#             if index < 0:
#                 index = self.n + index
#             if not (0 <= index < self.n):
#                 raise IndexError('invalid index')
#             elem = self.data_arr[index]
#             for i in range(index, self.n - 1):
#                 self.data_arr[i] = self.data_arr[i + 1]
#             self.data_arr[self.n - 1] = None
#             self.n -= 1
#             if self.n < self.capacity // 4 and self.capacity > 1:
#                 self.resize(self.capacity // 2)
#             return elem

# Q3 (a)
# def find_duplicates(lst):
#     n = len(lst)
#     freq = [0] * n
#     for num in lst:
#         freq[num] += 1
#     duplicates = []
#     for i in range(1, n):
#         if freq[i] > 1:
#             duplicates.append(i)
#     return duplicates

# Q4 (b)
def remove_all(lst, value):
    write_index = 0
    for read_index in range(len(lst)):
        if lst[read_index] != value:
            lst[write_index] = lst[read_index]
            write_index += 1
    for _ in range(len(lst) - write_index):
        lst.pop()