from math import sqrt
max_value = int(input("Enter the maximum number: "))
value = 2 #The least prime number

while value <= max_value:
    is_prime = True
    trial_factor = 2
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False
            break
        trial_factor += 1
    if is_prime:
        print(value,"  ",  end ='')
print()