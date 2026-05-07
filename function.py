# write one call multiple, code reusable, 
# syntax:-  creation/declaration
#           calling
# def is a keyword

# def fun_name(parameters):
#   function_body

# fun_name(arguments)       # to call function

# required :- def(keyword), fun_name, (), :
# optional :- parameters, arguments, return(keyword, and use to terminate)



# def add():
#     print('addition is: ',5+6)
#     # return 5+6

# add()
# print(add())

# x = add()
# print(x)


# in-built function :- made by python 
# user-defined function :- made by user
#                           1. With return :- i. with argument  ii. without argument
#                           2. With-out return :- i. with argument   ii. without argument



# 1. without argument and with return
# def i() :
#     return 'hello'

# i()
# print(i())


# 2. without argument and without return
# def i():
#     print('hello')

# i()
# print(i())


# 3. with argument and with return
# def i(x,y):
#     a= x+y
#     return a

# i(5,6)
# print(i(5,6))

# def great(name):
#     return f'Welcome {name}'

# x = input('Enter your Name: ')
# print(great(x))


# 4. with argument and without return
# def i(x,y):
#     a= x+y
#     print(a)

# i(5,6)
# print(i(5,6))

# def great(name):
#     print (f'Welcome {name}')

# x = input('Enter your Name: ')
# great(x)



# relation b/w parameter and argument

# 1. positional argument :- 

# def show(x,y,z):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# show(1,2,3)
# show()
# show(10)
# show(10,20)
# show(10,20,30,40)




# 2. default positional argument






# imp  3. variable length argument (*args)                  comes under packing(* args) and unpacking(** kwargs)
# 4. keyword positional argument
# 5. keyword default positional argument
# imp  6. variable length keyword argument (**kwargs)       comes under packing and unpacking