'''###Q1'''
def can_construct(word, letters):
    word_list = list(word)
    letter_list = list(letters)
    print(word_list)
    print(letter_list)
    works = False
    for i in letter_list:
        print(i)
        if i in word_list:
            word_list.remove(i)
            print(word_list)
            print(letter_list)
    if len(word_list)<1:
        works = True
    return works


#print(can_construct("apples","aples"))
#print(can_construct("apples","apleslp"))


'''-------------------------------------------------------------------------'''
'''###Q2'''

class complex():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return complex(self.a +other.a,self.b+other.b)
    def __sub__(self,other):
        return complex(self.a -other.a,self.b-other.b)
    def __mul__(self,other):
        return complex(self.a*other.a-self.b*other.b,        self.a*other.b+self.b*other.a)
    def __repr__(self):
        if self.b>0:
            out = str(self.a)+"+"+str(self.b)+"i"
            return out 
        elif self.b<0:
            out = str(self.a)+str(self.b)+"i"
            return out
        else:
            return str(self.a)
    def __iadd__(self,other):
        self = self+other
        return self
    
'''
cplx1 = complex(5, 2)
print(cplx1)          # 5 + 2i
cplx2 = complex(3, 3)
print(cplx2)          # 3 + 3i

# addition
print(cplx1 + cplx2)  # 8 + 5i

# subtraction
print(cplx1 - cplx2)  # 2 - 1i

# multiplication
print(cplx1 * cplx2)  # 9 + 21i

# original objects remain unchanged
print(cplx1)          # 5 + 2i
print(cplx2)          # 3 + 3i

# iadd
print(cplx1)          # 5 + 2i
cplx1 += cplx2
print(cplx1)          # 8 + 5i
'''



'''-------------------------------------------------------------------------'''
'''###Q3'''

from random import randint   
def create_permutation(n):
    lst = [i for i in range(n)]
    print(lst)
    for j in range(n):
        num = randint(0,(n-1))
        temp = lst[num]
        lst[num] = lst[j]
        lst[j] = temp   # a, b = b, s
    return lst

def scrambler(word):
    wordlst = list(word)
    n = len(wordlst)-1
    for j in range(n):
        num = randint(0,(n-1))
        temp = wordlst[num]
        wordlst[num] = wordlst[j]
        wordlst[j] = temp
    return "".join(wordlst)

def guesser():
    chances = 1
    word = scrambler("pokemon")
    out = "Unscramble the word:   "
    for i in word:
        out += i+"  "
    while chances<4:
        print(out)
        guess = input(("Try #"+str(chances)))
        if guess == "pokemon":
            print("good job")
            return
        else:
            print("try again")
            chances += 1
    print("failed")
    

#print(create_permutation(6))
#print(scrambler("hello"))
#print(guesser())