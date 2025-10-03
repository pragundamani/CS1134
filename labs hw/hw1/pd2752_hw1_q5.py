def fibs(n):
    fib1,fib2 = 0,1

    for _ in range(n):
        yield fib2
        fib1, fib2 = fib2, fib1+fib2


# for curr in fibs(8):
#     print(curr)
