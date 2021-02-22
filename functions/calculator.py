def help_screen():
    print("A: Adds n and m\
        S: Substracts n from m\
            M: Multiplies n amd m\
                D: Divides n and m\
                    H: Displays Helpscreen\
                        Q: Quits the program")
def menu():
    return input("\
        A: \
            S: \
                M: \
                    D: \
                        H: \
                            Q: \
                                ")

def add(n, m):
    return n + m

def sub(n, m):
    if n > m:
        return n - m
    return m - n

def mul(n ,m):
    return n * m

def div(n, m):
    if m > 0:
        return n / m

def main():
    n = int(input("Enter N: "))
    m = int(input("Enter M: "))
    
    results = 0.0
    done = False
    while not done:
        choice = menu()
        if choice == 'A' or choice == 'a':
            results = add(n, m)
            print(results)

        elif choice == 'S' or choice == 's':
            results = sub(n, m)
            print(results)

        elif choice == 'M' or choice == 'm':
            results = mul(n, m)
            print(results)

        elif choice == 'D' or choice == 'd':
            results = div(n, m)
            print(results)

        elif choice == 'H' or choice == 'h':
            help_screen()

        elif choice == 'Q' or choice == 'q':
            done = True
            
main()