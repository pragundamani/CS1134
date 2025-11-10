#q1 answer pd2752
from ArrayStack import ArrayStack

def postfix_calculator(exp):
    
    def is_var(s):
        return not(isinstance(s, int) or s in '+-*/=')
    
    def eval(token, numsstack):
        b = numsstack.pop()
        a = numsstack.pop()
        if token == '+':
            numsstack.push(a + b)
        elif token == '-':
            numsstack.push(a - b)
        elif token == '*':
            numsstack.push(a * b)
        elif token == '/':
            numsstack.push(a / b)

    numsstack = ArrayStack()
    vars, vars_vals = [], []
    tokens = exp.split()

    for token in tokens:
        if isinstance(token, int):
            numsstack.push(token)
        elif is_var(token):
            if token in vars:
                numsstack.push(vars_vals[vars.index(token)])
            else:
                val = tokens[tokens.index(token) + 4]
                vars.append(token)
                vars_vals.append(val)
                numsstack.push(val)
        elif token in '+-*/':
            eval(token, numsstack)
        elif token == '=':
            pass
    return numsstack.pop()

exp = "x 3 = y 4 = x y +"
result = postfix_calculator(exp)
print(result)  # Output should be 7
