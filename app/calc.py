def soma(a,b):
    return a + b

def subtrai(a,b):
    return a - b

def multiplica (a,b):
    a = a + 2
    return a*b

def divide (a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b