def ArrayStack():
    pass
def stack_sorter(s):
    helper = ArrayStack()
    for i in range(n, 0, -1):
        lowest = s.pop()
        for _ in range(i - 1):
            v = s.pop()
            if v < lowest:
                helper.push(lowest)
                lowest = v
            else:
                helper.push(v)
        s.push(lowest)
        while len(helper) > 0:
            s.push(helper.pop())