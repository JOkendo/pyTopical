d = {'Fred': 40, 'Ella' : 41, 'Zoe':39, 'Owen': 42}
print(d)

d['Jack'] = 44
print(d)

#keys()
for k in d.keys(): #for k in d:
    print(k)

#values()
for v in d.values():
    print(v)

#items()
for k,v in d.items():
    print(k,v)

lst = ['Fred','Kate', 'Owen']
lst1 = [123, 213, 331]
for t in zip(lst, lst1):
    print(t)
#using dict function
d1 = dict(zip(lst,lst1))
print(d1)