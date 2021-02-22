t = 3, 'A', 99, 16, 9
_, letter, _, _, quant = t
print(t)
lst = [1,2,3,4,5]
tpl = (6,7,8,9)
tpl1 = tuple(lst)
lst1 = list(tpl)
print(lst1)
print(tpl1)

lst3 = ['a','b','c','d','e']
lst2 = [2,4,6,8,10]

#Using zip() to generate tuples from two lists
for t in zip(lst, lst2):
    print(t, end='\n')

#Creating list using range and list
l = list(zip(range(5), range(5,11)))
print(l)


for p in zip(lst, lst2):
    print(p)
for (x,y) in zip(lst, lst2):
    print(x+y)
#Generating list out of two list using zip and list comprehension
l1 = [ x + y for (x, y) in zip(lst,lst2)]
print(l1)
