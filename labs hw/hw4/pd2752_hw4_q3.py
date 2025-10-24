#q3 answer pd2752
def print_triangle(n):
    for i in range(1,n+1):
        print('*'*i)
        
# print_triangle(5)

def print_opposite_triangles(n):
    for i in range(n,0,-1):
        print('*'*i)
    print_triangle(n)
        
# print_opposite_triangle(5)

def print_ruler(n):
    if n<=0:
        return
    if n == 1:
        print('-')
        return
    print_ruler(n-1)
    print('-' * n)
    print_ruler(n-1)

# print_ruler(4)


