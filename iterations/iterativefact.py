def factorial(n):
    product = 1
    while n:
        product *= n
        n -= 1
    return product

def main():
    print(factorial(10))

main()