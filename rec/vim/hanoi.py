# Rules:
# If even go to left
# If odd go to right
# If neither is possible move to stack not used in previous operation

# def hanota(A: list[int], B: list[int], C: list[int]) -> None:
#     def dfs(n, a, b, c):
#         if n == 1:
#             c.append(a.pop())
#             return
#         dfs(n - 1, a, c, b)
#         c.append(a.pop())
#         dfs(n - 1, b, a, c)
#     dfs(len(A), A, B, C)
#     return A,B,C


# def hanota(A: list[int], B: list[int], C: list[int]) -> None:
#     stk = [(len(A), A, B, C)]
#     while stk:
#         n, a, b, c = stk.pop()
#         if n == 1:
#             c.append(a.pop())
#         else:
#             stk.append((n - 1, b, a, c))
#             stk.append((1, a, b, c))
#         stk.append((n - 1, a, c, b))
#     return A,B,C

# print(hanota([5,4,3,2,1,0],[],[]))


