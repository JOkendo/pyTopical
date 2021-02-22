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

results = 0.0
n = 0
m = 0

def get_input():
    global n , m
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

def report():
    print(results)

def add():
    global results
    results = n + m

def sub():
    global results
    if n > m:
        results = n - m
    results = n - m

def mul():
    global results
    results = n * m

def div():
    global results
    if m > 0:
        results =  n / m

def main():
    done = False
    while not done:
        choice = menu()
        if choice == 'A' or choice == 'a':
            get_input()
            add()
            report()

        elif choice == 'S' or choice == 's':
            get_input()
            sub()
            report()

        elif choice == 'M' or choice == 'm':
            get_input()
            mul()
            report()

        elif choice == 'D' or choice == 'd':
            get_input()
            div()
            report()

        elif choice == 'H' or choice == 'h':
            help_screen()

        elif choice == 'Q' or choice == 'q':
            done = True
            
main()