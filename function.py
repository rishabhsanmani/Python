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

# syntax :-   def fun_name (per1=0,per2=0)
            
# fun_name(arg1,arg2)
# fun_name(arg1)
# fun_name()


# def add (x=0,y=0,z=0):
#     print(x+y+z)

# add()
# add(10)
# add(10,20)
# add(10,20,30)




# imp  3. variable length argument (*args)                  comes under packing(* args) and unpacking(** kwargs)

#                                       (* holds value in tuple it also work as packing and unpacking in list and tuple)

# syntax :-          def fun_name(*args)
#          fun_name(args)
#          fun_name(arg1,arg2,arg3)


# def display(*n):
#     print(n)
#     print(type(n))

# display()
# display(10,20)
# display(12,85,'rishabh')


# def display(*n):
#     sum=0
#     for i in n:
#         sum = sum+i
#     print(sum)

# display()
# display(10,20,30,40,50,60,70,80,90,100)


# def display(*n):        #  * behave like packing
#     print(n)
#     print(type(n))

# value = eval(input('Enter all values: '))
# display(value)
# display(*value)          #  * here behave like unpacking


# def natural_num(x):
#     for i in range(1,n+1):
#         print(i)

# n = int(input('Enter any number: '))
# natural_num(n)




# 4. keyword positional argument  =  (key=value)

# syntax :-  def fun_name(par1,par2,...)

#            fun_name(par1=value,par2=value)

# def add(x,y,z):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# add(x=40,y=50,z=60)
# add()
# add(x=10)
# add(x=10,y=100)
# add(x=10,y=100,a=50,z=98,c=69,v=911)




# 5. keyword default positional argument

# def add(x=0,y=0,z=0):
#     print('x:',x)
#     print('y:',y)
#     print('z:',z)
# add(x=40,y=50,z=60)
# add()
# add(x=10)
# add(x=10,y=100)
# add(x=10,y=100,a=50,z=98,c=69,v=911)




# imp  6. variable length keyword argument (**kwargs)       comes under packing and unpacking

# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# add(x=40,y=50,z=60)
# add()
# add(x=10)
# add(x=10,y=100)
# add(x=10,y=100,a=50,z=98,c=69,v=911)

# def add(**kwargs):
#     sum=0
#     for i in kwargs:
#         sum+=kwargs.get(i)
#     print(sum)

# d = eval(input('Enter data in dictionary: '))
# add(**d)

