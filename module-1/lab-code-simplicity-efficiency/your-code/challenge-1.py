"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
def get_input():
    numbers = range(6)
    signs = ['+','-']
    a = int(input('Please choose your first number (0 to 5): '))
    while a not in numbers:
        a = int(input("Choose a number from 0 to 5."))
    b = input('What do you want to do? + or -: ')   
    while b not in signs:
        b = input('Choose + or -: ')
    c = int(input('Please choose your second number (0 to 5): '))
    while c not in numbers:    
        c = int(input("Choose a number from 0 to 5."))
    return a, b, c

def operation(first, sign, second):
    return (first + second if sign =='+' else first- second)

def result(answer):
    return f'The result of {first} {sign} {second} is {answer}'

first, sign, second = get_input()
answer = operation(first, sign, second)
print(result(answer))
print("Thanks for using this calculator, goodbye :)")

