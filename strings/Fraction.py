import mysql.connector
from fractions import Fraction
mydb = mysql.connector.connect(
    host = "localhost"
    user = "okendo"
    password = "kkkkz"
)
print(mydb)

f = Fraction(3, 4)
f1 = Fraction(1, 2)

add = f.__add__(f1)
sub = f.__sub__(f1)
mul = f.__mul__(f1)
div = f.__truediv__(f1)

print(add, sub, mul, div)