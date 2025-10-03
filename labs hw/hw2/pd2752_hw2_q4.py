#q4 answer pd2752
# def e_approx(n):
#     if n <=0: return 0
#     lst = [1/sum([j for j in range(1,i)]) for i in range(1,n)]
#     return sum(lst)+1

def e_approx(n):
    if n==0:return 0
    total, fact, num = 1, 1, 1
    while num<=(n+1):
        # print(total,fact,num)
        fact *= num
        total += 1/fact
        num += 1
    return total



# def main():
#     for n in range(15):
#         curr_approx = e_approx(n)
#         approx_str = "{:.15f}".format(curr_approx)
#         print("n =", n, "Approximation:", approx_str)
# main()