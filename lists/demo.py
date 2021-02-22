lst = [2,4,76,"Anya", "Kwenda",list([1,2,3,4])]
print(lst)
lst = [2,4,5,6,8,9,15]
for elem in lst:
    print(elem ,end='  ')
print()

#Reverse
lst = [2,4,5,6,8,9,15]
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=' ')
print()

lst1 = [2,3,4]
lst2 = [7,8]
print(lst1 + lst2)