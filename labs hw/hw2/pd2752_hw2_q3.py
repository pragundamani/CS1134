#q3 answer pd2752
def factors(num):
    results = []
    for i in range(1,int(num**0.5)+1):
        if num%i == 0:
            yield i
            results.append(i)
    for i in range((len(results)-2),0,-1):
        yield (num//results[i])
    yield num

# for curr_factor in factors(100):
#     print(curr_factor)



