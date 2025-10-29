from ArrayStack import ArrayStack

def eval_postfix(expr):
    operators = "+-*/"
    valstack = ArrayStack()
    exp_list = expr.split()
    for token in exp_list:
        if token not in operators:
            valstack.push(float(token))
        else:
            if token == "+":
                valstack.push(valstack.pop() + valstack.pop())
            elif token == "-":
                valstack.push(-valstack.pop() + valstack.pop())
            elif token == "*":
                valstack.push(valstack.pop() * valstack.pop())
            elif token == "/":
                valstack.push(1 / valstack.pop() * valstack.pop())
    return valstack.pop()



