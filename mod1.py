def add(x,y):
    return x + y

result = add(3,5)
print(result)

def min(a,b):
    return a - b

result = min(3,5)
print(result)

def mult(q,v):
    return q * v

result = mult(3,5)
print(result)

def dev(c,d):
    return c / d

result = dev(3,5)
print(result)

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return min(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return dev(tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")


expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:", result)