'''Lists and Functions'''
'''summing up list items'''
def sum(lst):
    result = 0
    for items in lst:
        result += items
    return result

'''Make list zero'''
def make_zero(lst):
    for item in range(len(lst)):
        lst[item] = 0
'''Make random list'''
def random_list(n):
    import random
    result = []
    for i in range(n):
        rand = random.randrange(100)
        result += [rand]
    return result

def main():
    rand = random_list(4)
    print(rand)

    su = sum(rand)
    print(su)
    make_zero(rand)
    print(rand)
    

main()