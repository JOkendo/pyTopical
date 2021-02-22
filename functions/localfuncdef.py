'''To demostrate the local function definition
The concept demonstrates functional decomposition and
at the same time upholding functional encapsulation.'''

from math import fabs

'''The enclosing function calculates the surface area of the 3D box
The function accepts 8 points of the box's vertices.'''

def surface_area(
    x, y, z, x1, y1, z1, 
    x2, y2, z2, x3, y3, z3, 
    x4, y4, z4, x5, y5, z5, 
    x6, y6, z6, x7, y7, z7
    ):
   

    '''Area of each face'''
    def area(l, w):
        return l * w
    length = fabs(x7 - x6)
    height = fabs(y4 - y3)
    front_area = area(length, height)
    
    width = fabs(z5 - z4)
    side_area = area(width, height)

    top_area = area(width, length)


    return 2*front_area + 2*side_area + 2*top_area


'''Get points in terms of tuple, and print a message'''
def get_points(msg):
        print(msg)
        x = int(input("x coordinate: "))
        y = int(input("y coordinate: "))
        z = int(input("z coordinate: "))
        return x, y, z

print("Enter the points: ")
x, y,z = get_points("1: ")
x1,y1,z1 = get_points("2: ")
x2, y2,z2 = get_points("3: ")
x3, y3,z3 = get_points("4: ")
x4, y4,z4 = get_points("5: ")
x5, y5,z5 = get_points("6: ")
x6, y6,z6 = get_points("7: ")
x7, y7,z7 = get_points("8: ")

'''Local counter'''
#Using the nonlocal keyword
def counter():
    count = 0
    def ctr(): #Local function
        nonlocal count
        while count < 8:
            print(count, end=' ')
            count += 1
        return count
    return ctr # Returns a function

def main():
    print("Surface Area: ", surface_area(
    x, y, z, x1, y1, z1, 
    x2, y2, z2, x3, y3, z3, 
    x4, y4, z4, x5, y5, z5, 
    x6, y6, z6, x7, y7, z7
    ))

c = counter()
print(c())
main()