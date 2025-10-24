#q5 answer pd2752
def count_lowercase(s,low,high):
    if low>high:
        return 0
    count = 0
    for i in range(low,high+1):
        if s[i].islower():
            count+=1
    return count

# print(count_lowercase("Hello World", 0 ,10)) 

def is_number_of_lowercase_even(s,low,high):
    return count_lowercase(s,low,high)%2==0

# print(is_number_of_lowercase_even("Hello World", 0 ,10))
# print(is_number_of_lowercase_even("Hello World!", 0 ,9))