MAX = 500
nonprimes = MAX * [False]
nonprimes[0] = nonprimes[1] = True
for i in range(2, MAX + 1):
    if not nonprimes[i]:
        print(i, end=' ')
        for j in range(2 * i, MAX + 1, i):
            print(nonprimes[j])
print()
