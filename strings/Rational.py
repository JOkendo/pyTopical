 
class Rational:
    def __init__(self, numerator = 1, denominator = 0):
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)

    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    def __sub__(self, secondRational):
        n = self.__numerator * secondRational[1] - self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0]
        return Rational(n, d)

    def __float__(self):
        return self.__numerator / self.__denominator
    
        
    def __int__(self):
        return int(self.__float__())
        
    '''def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + self.__denominator)
            '''
    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0
        
    def __le__(self, secondRational):
        return self.__cmp__(secondRational) <= 0
    
    def __gt__(self, secondRational):
        return self.__cmp__(secondRational) > 0
        
    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >= 0
        
    # Compare two numbers
    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0
            
    # Return numerator and denominator using an index operator
    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator


'''GCD use to reduce the fraction to its simplest form'''

def gcd(n,d):
    if d == 0:
        return n
    else:
        return gcd(d, n % d)
