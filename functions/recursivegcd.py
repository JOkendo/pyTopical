def recursivegcd(m, n):
    """Returns the GCD of m and n"""
    if n == 0:
        return m
    else:
        return recursivegcd(n, m % n)

def main():
    gcd =recursivegcd(8, 10)
    print(gcd)
main()