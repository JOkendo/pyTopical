from recursivegcd import recursivegcd

"""Making functions Reusable"""
def recursivefib(n):
    """Returns the nth fibinacci number in the series"""
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursivefib( n - 2 ) + recursivefib( n - 1 )

def main():
    recursivegcd(4,30)
    fib = recursivefib(10)
    print(fib)
main()