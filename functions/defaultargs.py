'''Default arguments'''
def count(m = 10):
    for i in range(1,m + 1):
        print(i, " ", end='')
    print()


def counting(m, n = 5):
    for i in range(m,n + 1):
        print(i, " ", end='')
    print()


def main():
    count()
    count(7)
    counting(2)
    counting(2, 8)

main()