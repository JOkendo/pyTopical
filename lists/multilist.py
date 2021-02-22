matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(matrix[1][2])
for row in matrix:
    for column in row:
        print('{:>4}'.format(column),end='')
    print()
print()

ragged = [[2,3,4,5,6],
          [3,4,5],
          [6,8,9,5,3]]
for row in ragged:
    for elem in row:
        print(elem, end='   ')
    print()

a = [[1,2] * 2 for x in range(3)]
print(a)
a1 = [[0 for _ in range(4)]for _ in range(3)]
print(a1)