#pd2751
from ArrayStack import ArrayStack

def evaluate_postfix(tokens, var_names, var_values):
    stack = ArrayStack()
    for token in tokens:
        if token in '+-*/':
            b = float(stack.pop())
            a = float(stack.pop())
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            if token.lstrip('-').isdigit():
                stack.push(int(token))
            else:
                val = None
                for i, name in enumerate(var_names):
                    if name == token:
                        val = var_values[i]
                        break
                stack.push(val)
    return stack.pop()

def set_var_value(name, value, var_names, var_values):
    for i, v in enumerate(var_names):
        if v == name:
            var_values[i] = value
            return
    var_names.append(name)
    var_values.append(value)

def format_number(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

var_names = []
var_values = []

while True:
    line = input("--> ").strip()
    if line == "done()":
        break
    if not line:
        continue
    tokens = line.split()
    if len(tokens) >= 2 and tokens[1] == '=':
        var_name = tokens[-1]
        value = evaluate_postfix(tokens[1:], var_names, var_values)
        set_var_value(var_name, value, var_names, var_values)
        print(var_name)
    else:
        value = evaluate_postfix(tokens, var_names, var_values)
        print(format_number(value))
