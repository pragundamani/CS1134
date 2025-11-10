#q1 answer pd2752
from ArrayStack import ArrayStack

def postfix_calculator(exp):
    
    def is_var(s):
        flag1 = not isinstance(s, int)
        flag2 = str(s) not in '+-*/='
        return flag1 and flag2

    
    def eval(token, numsstack):
        b = (numsstack.pop())
        a = int(numsstack.pop())
        print(a,b)
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
        try:
            token = int(token)
            numsstack.push(token)
        except:
            print(token,is_var(token))
        
        if is_var(token):
            if token in vars:
                numsstack.push(vars_vals[vars.index(token)])
            else:
                val = tokens[tokens.index(token) + 2]
                print(val)
                vars.append(token)
                vars_vals.append(val)
                numsstack.push(val)
        elif str(token) in '+-*/':
            eval(token, numsstack)
        elif token == '=':
            pass

    return numsstack.pop()

exp = ""
while exp != 'done()':
    exp = input("--> ")
    print(postfix_calculator(exp))

