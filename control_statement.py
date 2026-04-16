# Control Statement :- it is divided into 3 parts

# 1. conditional statement :- if, if-else, if-elif, if-elif-else
# 2. itrating/ looping statement :- while, while-else, for, for-else
# 3. transfer statement :- continue, break, pass

# elif is a dependent on if

# ----------------------------------------------------------------------------------------------------


# conditional statement :-

# i :- if-statement :- syntax :- if condition :
#                                    |
#                                    |if-body executed when given condition is true
#                                    |
# Note :- block may be executed

# Example
# if 10:
#     print('Hello')


# n = eval(input("Enter any number : "))
# if n%2==0 :
#     print(f'Given Number {n} is Even')
# print("Thanks")


# ii :- if-else statement :-


# n = eval(input("Enter any number : "))
# if n%2==0 :
#     print(f'Given Number {n} is Even')
# else:
#     print(f'Given Number {n} is not Even')


# n = eval(input("Enter any number : "))
# if n==0 :
#     print(f'Given number {n} is Zero')
# elif n%2==0 :
#     print(f'Given number {n} is Even')
# elif n%2!=0 :
#     print(f'Given number {n} is Odd')

# n = eval(input("Enter any number : "))
# if n==0 :
#     print(f'Given number {n} is Zero')
# elif n<0 :
#     print(f'Given number {n} is negative')
# elif n%2==0 :
#     print(f'Given number {n} is Even')
# elif n%2!=0 :
#     print(f'Given number {n} is Odd')

r = eval(input('Enter Radius : '))
if r>0 :
    a = 3.14*r**2
    print(f'Area of circle is {a}')
else:
    print("Given number is nevative Please enter positive number")

