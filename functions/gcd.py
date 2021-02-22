'''Program to print the GCD of two integers'''
def gcd(n1, n2):
    min = n1 if n1 < n2 else n2
    gcd = 1 # Default GCD for all numbers.

    for i in range(1, min+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
'''def main():
    gcd(12, 45)

main()'''