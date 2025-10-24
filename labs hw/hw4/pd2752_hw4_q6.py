#q6 answer pd2752
def appearances(s,low,high):
    if low>high:
        return {}
    counts = appearances(s,low,high-1)
    char = s[high]
    if char in counts:
        counts[char] = counts[char]+1
    else:
        counts[char] = 1
    return counts


# print(appearances("banana",0,5))
# print(appearances("abbaca",0,5))