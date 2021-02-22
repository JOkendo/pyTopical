def make_list():
    result = []
    in_value = 0
    while in_value >= 0:
        in_value = int(input("List Items: "))
        if in_value >= 0:
            result += [in_value]
    return result

def main():
    col = make_list()
    print(col)
'''Mking list from range object'''
lst = list(range(0,1))
print(lst * 5)

#in ... not in...operator
k = list(range(2,5))
for i in range(2, 8):
    if i in k:
        print(i, " member of ", k)
    if i not in k:
        print(i, " not member of ", k)


a = [2,3,4]
b = [6, 8, 7]
b[1] = 89
b = a
print(a)

#Aliasing
a = [1,2,3]
b = [1,2,3]
print('Is ', a, 'equal to ', b, ' ? ', a == b )
print('Is ', a, 'alias to ', b, ' ? ', a is b )

a = b
print('Is ', a, 'equal to ', b, ' ? ', a == b )
print('Is ', a, 'alias to ', b, ' ? ', a is b )
 

#Making list copy
def copy_list(lst):
    result = []
    for item in lst:
        result += [item]
    return result

x = [2,3,4]
y = copy_list(x)
print('Y: ', y)
r = range(10)
print(r)
f = list(r)
print(f)


#Slicing
#Easiest way of making a copy of a list
cop = f[:]
print(cop)

#copy in reverse
copr = f[::-1]
del copr[2 : 7]
print(copr)
#main()