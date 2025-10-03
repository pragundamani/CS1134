'''Q1'''
# False because n^3 is more than to n^2logn
# False logn is less than sqrt(n)
# True sqrt(n) is less than /logn
# False 100^n is more than n!

'''Q2'''
# n = theta(n)
# 2n^2-n = theta(n^2)
# n^2 = theta(n^2)
# log(n)^2 = theta log(n)^2 

'''Q3'''
# a -> n, will run n times for outer loop
# b -> n, will run n times for outer loop
# c -> n^2, will run 0.5n * n times 
# d -> sqrt(n)*n, since outer loop is sqrt(n) and inner loop will run n times 
# e -> n^3, will run n*n*n times

'''Q4'''
# a -> n^2, run n*n times
# b -> n^2, will run n*n 
# c -> n, will run n times for outer loop
# d -> n * log(n), will run n times for outer loop and log(n) for inner loop 
