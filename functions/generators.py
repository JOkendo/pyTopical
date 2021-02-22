from math import sqrt #used to test for primality.


"""Using global to remember a function"""
count = 0
def remember():
    global count
    count += 1
    print("Calling remember: " + str(count))

"""Generators basics"""
def gen():
    yield 1
    yield 'wow'
    yield -2

"""Use yield in a loop"""
def gen_mult(m,n):
    count = 0
    while count < n:
        yield count * m
        count += 1
        
'''Built-in range function'''
def my_range(start, Stop=None, step=1):
    #When we have both start and end;
    if Stop != None:
        begin = start
        end = Stop
    else:
        begin = 0
        end = start
    i = begin
    while i != end:
        yield i
        i += step

"""Generating prime numbers"""
#Test primality
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    trial_factor = 3
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:
            return False
        trial_factor =+ 2
    return True

#prime sequence
def prime_seq(begin, end):
    for value in range(begin, end + 1):
        if is_prime(value):
            yield value


def main():
   remember()
   remember()
   x = gen()
   print(next(x))
   print(next(x))
   print(next(x))
   

   """Using for loop"""
   for i in gen():
       print(i)
    

   '''Implementing the while loop'''
   for mult in gen_mult(6, 10):
      print(mult, end = ' ')
   print()    

   #My Range
   print("40 to 10: ", end = ' ' )
   for i in my_range(40, 90, 5):
      print(i, end=' ')
   print()

   print("40 to 90: ", end = ' ' )
   for i in my_range(40, 91, 10):
       print(i, end=' ')
   print()

  

main()