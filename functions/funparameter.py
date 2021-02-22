"""Using functions as parameters"""
def add(x, y):
    """Adds x and y"""
    return x + y
def mul(x, y):
    """Multiplies x and y"""
    return x * y
def evaluate(f, x ,y):
    """Uses a function f that evaluates x and y"""
    return f(x, y)

def main():
    print(add(9, 3))
    print(mul(4, 5))
    print(evaluate(mul, 4, 6))
    print(evaluate(add, 1, 9))
main()