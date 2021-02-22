def make_adder():
    loc_var = 2
    return lambda x : x + loc_var

def main():
    y = make_adder()
    print(y(10))

"""Defining and invoking the lambda expression at once."""
print((lambda x, y: x * y)(2, 3))
main()