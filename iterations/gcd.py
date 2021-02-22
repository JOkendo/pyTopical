#GCD
a = int(input("Enter a: "))
b = int(input('Enter b: '))

gcd = 1 #initial gcd
k = 2 #possible gcd
while k <= a and k <= b:
    if a%k == 0 and b%k == 0:
        gcd = k
    k += 1
print(gcd)