def sum_of_squares(n):
    total = 0

    # for i in range(n):
    #     total += i**2

    total = sum(i**2 for i in range(n))
    
    return total


print(sum_of_squares(4))
print(sum_of_squares(5))

def sum_of_squares_odd(n):
    total = 0
    if n%2==1:
        n-=1
    total = sum(i**2 for i in range(1,n,2))
    return total

print(sum_of_squares_odd(4))
print(sum_of_squares_odd(5))


