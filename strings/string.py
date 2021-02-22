"""
PALINDROME
Palindrome is a word that reads the same foward and backward.


Checking a palindrome
"""
import sys
def isPalindrome(s):
    low = 0
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False
        
        low += 1
        high -= 1
    return True

def main():
    done = False
    while not done:
        an = input("Y or N: ")
        if an == 'y':
            s = input("Enter s: ").strip()
            if isPalindrome(s):
                print(s, " \"is a palindrome\" ")
            else:
                print(s, " \"is not a palindrome\" ")
        elif an == 'n':
            done = True
        

main()