import string
import random
"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')


def RandomStringGenerator(l=12, a=(list(string.ascii_lowercase) + list(str(i) for i in range(0,10)))):
    p = 0
    s = ''
    while p<l:
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(int(n)):
        if int(a) < int(b):
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            raise Exception("Incorrect min and max string lengths. Try again.")
        r.append(RandomStringGenerator(c))
    return r

print(BatchStringGenerator(int(n), int(a), int(b)))
