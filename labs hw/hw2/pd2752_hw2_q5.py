def split_parity(lst):
    odds = [i for i in lst if i%2 != 0]
    evens = [j for j in lst if j%2 == 0]
    return (odds + evens)

print(split_parity([1,2,3,4]))
