'''List comprehension'''

#List of perfect squares less than 50
p = [0,1,4,9,16,25,36,49]

p = [x**2 for x in [0,1,2,3,4,5,6,7]]
print(p)
p = [x**2 for x in range(8)]
print(p)
lst = list(range(4,41,4))
print(lst)
h = [x/2 for x in range(0, 11, 2)]
print(h)
lst = [23,45,44,23,-4, -9,56]
print(lst)
new = [x for x in lst if x>=0]
print(new)

string = [2,3, 5, 're', 'wow', 9]
stri = [x for x in string if type(x) != str]
print(stri)

#Generate tuple
square = [(x, x**2) for x in range(1,11)]
print(square)

#Using two for statements to extract elements from 2 lists
k = [1,2,3]
n = [5,7,9]

m = [(x,y)for x in k for y in n if x != y]
print(m)

z = ['wow', 'thanks', 'kech']
t = [{x:y} for x in k for y in z]
print(t)