from ArrayStack import *

variables = {}


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_var(s):
    return s in variables


while True:
    exp = input("--> ")
    exp_list = exp.split()
    last_var = None

    if exp == "done()":
        break

    stack = ArrayStack()

    for i in range(len(exp_list)):
        if is_number(exp_list[i]):
            stack.push(int(exp_list[i]))
        elif is_var(exp_list[i]):
            stack.push(variables[exp_list[i]])
        elif exp_list[i] in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if exp_list[i] == '+':
                stack.push(a + b)
            elif exp_list[i] == '-':
                stack.push(a - b)
            elif exp_list[i] == '*':
                stack.push(a * b)
            elif exp_list[i] == '/':
                stack.push(a / b)
        elif exp_list[i] == "=":
            last_var = exp_list[i-1]

    if not last_var is None:
        variables[last_var] = stack.pop()
        print(last_var)
    else:
        print(stack.pop())
