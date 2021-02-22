def sum(*num):
    result = 0
    for n in num:
        result += n
    return result
s = sum(*(2,3,4,5))
print(s)

tpl = 1,2,3,4,5,6,7

#Demostrate general unpacking; this also happens with lists
t, p, *rest = tpl
print(t)
print(p)
print(*rest) #Print just the list elements