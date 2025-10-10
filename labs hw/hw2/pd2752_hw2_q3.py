#q3 answer pd2752
def factors(num):
    results = []
    for i in range(1,int(num**0.5)+1):
        if num%i == 0:
            yield i
            results.append(i)
    for i in range((len(results)-2),0,-1):
        yield (num//results[i])
    if num>1: 
        yield num



# for curr_factor in factors(1):
#     print(curr_factor)



