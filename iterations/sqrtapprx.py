'''Square root approximation to demstrate 
the use of While loop'''

value = int(input('Enter value to approximate its root: '))

#Guess a root
root = 1.0

diff = root * root - value

while diff > 0.0000001 or diff < -0.0000001:
    root = (root + value / root) / 2
    diff = root * root - value
print(root)