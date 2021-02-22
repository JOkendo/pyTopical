'''Decorators
Used for the purposes of testin a program
Denoted by appending the @ symbol before the decorating function.
i,e; @show_call_and_return_details

DECORATORS HELP ADD FUNCTIONALITY TO FUNCTIONS BY:
i) Passing the function to the decorator function as a paramenter
ii) Defining the replica of the said function local to the decorator
iii) Decorator returning the function in (ii) above to itself.


NB: Decoration is achieved by integrating;
passing functions as arguments, defining local functions 
and returning functions' capabilities in python
'''

def show_call_and_return_details(f):
    func_name = f.__name__ #finding the function's name
    
    '''local funct'''
    def execute_augmented(x, y): #Local function
        call_string = "{}({} {})".format(func_name, x, y)
        print(">> Calling " + call_string)
        result = f(x, y)
        print("<<  Returning {} from " . format(result) + call_string)
        return result
    return execute_augmented

'''Returning the maximum of two.'''
@show_call_and_return_details
def max(x, y):
    return x if x > y else y

'''GCD of two numbers'''
@show_call_and_return_details
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

'''summation of two numbers'''
@show_call_and_return_details
def summation(x, y):
    sum = 0
    while x != y:
        sum += x
        x += 1
    return sum

'''A decorator to deactivate a function'''
def nullify(f):
    fname = f.__name__
    def deactivate(x, y):
        pass
    return deactivate
@nullify
def add(x, y):
    return x+ y

def main():
    max(30, 45)
    print('........')

    gcd(34, 56)
    print('.......')

    summation(24, 54)
    print('........')

    add(3, 2)
    print('.......')

if __name__ == "__main__":
    main()