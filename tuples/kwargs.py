def f(a,b,c):
    print('a = ', a, 'b = ', b, 'c = ', c)

f(1,2,3)
d = {}
d['a'] = 11
d['b'] = 14
d['c'] = 20
f(**d)
f(**{'a':23, 'b' : 43, 'c' : 78})

#All variable names must be same