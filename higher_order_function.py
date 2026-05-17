# Functions of Hingher order function
# map()
# filter()
# reduce()
# decorator()

# lambda
# genarator
# file-handling
# module __package__ library
# OOPs
# exception handling


# 1. Map()

# syntax :- 

# iterable1 -------------
# iterable2 -------------

# def fun_name(n1,n2,...):
#     fun_body

# map(fun_name(iterable1,iterable2))
# map(fun,iterable)

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = [1,2,3,4]

# def sum(n1,n2,n3):
#     return n1+n2+n3

# res = map(sum,l1,l2,l3)
# print(res)
# print(list(res))
                            #   or
# res = list(map(sum,l1,l2,l3))
# print(res)



# -----------------------------------------------------



# 2. Filter function

# syntax :- 

# iterable
# def fun_name(n):
#     conditional statement

# res = list(filter(fun_name,iterable))
# filter(fun_name,iterable)            



# l = [1,2,3,4,5,6,7,8]

# def even(n):
#     if n%2==0:
#         return n
    
# def odd(n):
#     if n%2!=0:
#         return n

# res = tuple(filter(even,l))
# print(res)
# res1 = tuple(filter(odd,l))
# print(res1)


# l = [1,2,3,4,5,6,7,8]

# def show(n):
#     if n%2==0:
#         return 'Even'
#     else :
#         return 'Odd'

# res = list(map(show,l))
# print(res)



# ---------------------------------------------



# 3. Reduce function

# syntax :-

# import functools
# iterable
# def fun_name(n1,n2):
#     fun_body
# res = functools.reduce(fun_name,iterable)


# import functools
# l = [1,2,3,4,5]
# def add(a,b):
#     return a+b
# red = functools.reduce(add,l,0)
# print(red)
# res = functools.reduce(add,l)
# print(res)


# import functools
# l = [10,5,20,30,15,12]
# def max(a,b):
#     if a>b:
#         return a
#     else :
#         return b
# res = functools.reduce(max,l)
# print(res)

# import functools
# l = [10,5,20,30,15,12]
# def min(a,b):
#     if a<b:
#         return a
#     else :
#         return b
# res = functools.reduce(min,l)
# print(res)



# ---------------------------------------------------



# 4. Lambda function :- function which we have to use a single time

# syntax :-  lambda variable : singl_line_expression
#              ^
#              |
#           keyword

# x = lambda a,b : a+b
# x(5,10)
# print(x(5,10))

# x = lambda a : print(a**2)
# x(5)
# x(10)




# Map with lambda

# l=[1,2,3,4]

# res = list(map((lambda n : n**2),l))

# print(res)


# l1 = eval(input('Enter 1st list : '))
# l2 = eval(input('Enter 2nd list : '))
# l3 = eval(input('Enter 3rd list : '))
# res = list(map((lambda a,b,c : a+b+c),l1,l2,l3))
# print(res)



# --------------------------------------------------------



# Filter with lambda

# l1 = eval(input('Enter 1st list : '))
# res = list(filter((lambda a : a%2==0 ),l1))
# res = list(filter((lambda a : a if a%2==0 else None),l1))
# print(res)



# ---------------------------------------------------------



# Reduce with lambda 

# import functools
# from functools import reduce
# l = eval(input('Enter list: '))
# res = reduce((lambda a,b : a if a>b else b ),l)
# print(res)


# from functools import reduce
# l = eval(input('Enter list : '))
# res = reduce((lambda a,b : a if a<b else b),l)
# print(res)


