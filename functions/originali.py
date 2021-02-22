import importlib
from time import clock
for i in range(2):
    module = input("Enter module to import")
    importlib.import_module(module)

start = clock()
print(iterativefact(27))
end = clock()
elapsed = end - start
print(elapsed)

start = clock()
print(recursivefactorial(27))
end = clock()
elapsed = end - start
print(elapsed)