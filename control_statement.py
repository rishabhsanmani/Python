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

# r = eval(input('Enter Radius : '))
# if r>0 :
#     a = 3.14*r**2
#     print(f'Area of circle is {a}')
# else:
#     print("Given number is nevative Please enter positive number")



# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-



# Itrating Statement or looping Statement :- to avoid the repetation of block of code

# i.  while loop :- (infinite iteration)
# ii. for loop :- (finite iteratoin) use of collection datatype


# i. while loop :- Syntax =  while condition:
#                                  |
#                                  |While-code body
#                                  | 

# while True:
#     print("hello")

# n = eval(input('kitne baar run karna hai batao: '))
# i = 1
# while i<=n:
#     print(i, end=",")
#     i+=1

# n = eval(input('kitne baar run karna hai batao: '))
# i = 1
# while i<=n:
#     if i<n:
#         print(i,end=",")
#     else :
#         print(i)
#     i+=1

# n = eval(input('kitne baar run karna hai batao: '))
# i = 1
# while i<=n:
#     if i<n:
#         print(i,end="+")
#     else :
#         print(i)
#     i+=1

# n = eval(input('kitne baar run karna hai batao: '))
# i = 1
# while i<=n:
#     if i<n:
#         print(i,end="+")
#     else :
#         print(i,end='=')
#     i+=1

# n = eval(input('kitne baar run karna hai batao: '))
# sum,i = 0,1
# while i<=n:
#     sum = sum+i
#     if i<n:
#         print(i,end="+")
#     else :
#         print(i,end='=')
#     i+=1
# print(sum)    

# n = eval(input('kitne baar run karna hai batao: '))
# multiple,i = 1,1
# while i<=n:
#     multiple = multiple*i
#     if i<n:
#         print(i,end="*")
#     else :
#         print(i,end='=')
#     i+=1
# print(multiple)  



# n = eval(input('kitne baar run karna hai batao: '))
# i = 1
# while i<=n:
#     if i%2==0:
#         if i<n-1:
#             print(i,end=",")
#         else:
#             print(i)
#     i+=1

# n = eval(input('kitne baar run karna hai batao: '))
# sum,i = 0,1
# while i<=n:
#     if i%2==0:
#         sum = sum + i
#         if i<n-1:
#             print(i,end=",")
#         else:
#             print(i,end='=')
#     i+=1
# print(sum)

# n = eval(input('kitne baar run karna hai batao: '))
# multiple,i = 1,1
# while i<=n:
#     if i%2==0:
#         multiple = multiple * i
#         if i<n-1:
#             print(i,end=",")
#         else:
#             print(i,end='=')
#     i+=1
# print(multiple)


# n = eval(input('Enter number: '))
# i = 1
# while i<=n:
#     if i%2!=0:
#         if i<n-1 :
#             print(i,end=',')
#         else:
#             print(i)
#     i+=1

# n = eval(input('Enter number: '))
# sum,i = 0,1
# while i<=n:
#     if i%2!=0:
#         sum+=i
#         if i<n-1 :
#             print(i,end=',')
#         else:
#             print(i,end='=')
#     i+=1
# print(sum)

# n = eval(input('Enter number: '))
# multiple,i = 1,1
# while i<=n:
#     if i%2!=0:
#         multiple*=i
#         if i<n-1 :
#             print(i,end=',')
#         else:
#             print(i,end='=')
#     i+=1
# print(multiple)







# n = eval(input('Enter any number: '))
# t = 0
# while n>0:
#     t += 1
#     n//=10
# print(f'total digit are: {t}')


# n = eval(input('Enter any number: '))
# t,sum = 0,0
# while n>0:
#     t += 1
#     n//=10
#     sum = sum+t
# print(f'Sum of all digits are: {sum}')

# n = eval(input('Enter any number: '))
# sum = 0
# while n>0:
#     ld = n%10
#     sum = sum+ld
#     n = n//10
# print(f'Sum of all the digit: {sum}')



# -------------------------------------



# Armstrong :-

# n = eval(input('Enter any number: '))
# x,y,td=n,n,0
# while n>0:
#     td+=1
#     n//=10
# sum = 0
# while x>0:
#     ld = x%10
#     sum += ld**td
#     x//=10
# print(f'Sum of the number {sum}')
# if sum==y:
#     print(f'Given number {y} is Armstrong ')
# else:
#     print(f'Given number {y} is not Armstrong')



# -------------------------------------------------------------------



# Pallindrom

# for string
# n = input('Enter any number: ')
# if n==n[::-1]:
#     print(f'Given number {n} is Pollindrom')
# else:
#     print(f'Given number {n} is not Pollindrom')


# for integer
# n = eval(input('ENter any number: '))
# rev,x=0,n
# while n>0:
#     ld = n%10
#     rev = rev*10+ld
#     n//=10
# print(f'Number after reverse is {rev}')
# if rev==x:
#     print(f'Given number {x} is Pollindrom')
# else:
#     print(f'Given number {x} is not Pollindrom')



# --------------------------------------------------------------------



# Pattern

# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print('*'*n)
#     i+=1


# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print('*'*i)
#     i+=1

# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print('*'*i+' '*(n-i))
#     i+=1

# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1

# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1

# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print(' '*(n-i)+' *'*i)
#     i+=1


# n = eval(input('Enter number: '))
# i=0
# while i<n:
#     print('*'*(n-i)+' '*i)
#     i+=1

# n = eval(input('Enter number: '))
# i=0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1

# n = eval(input('Enter number: '))
# i=0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1


# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print('*'*i+' '*(n-i))
#     i+=1
# i-=2
# while i>0:
#     print('*'*i+' '*(n-i))
#     i-=1


# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1
# i-=2
# while i>0:
#     print(' '*(n-i)+'*'*i)
#     i-=1


# n = eval(input('Enter number : '))
# i=1 
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1
# i-=2
# while i>0:
#     print(' '*(n-i)+'* '*i)
#     i-=1



# ---------------------------------------------------------------------



# For Loop:-  syntax =>    for variable in iterables :
#                                for-body


# s= eval(input('Enter any character: '))
# x = ord(s)          # character to ascci
# print(x)
# y=x+2
# print(y)
# print(chr(y))       # ascii to character 


# ch = eval(input('Enter any character: '))
# print(chr(ord(eval(input('Enter any character: ')))+2))


# s = eval(input('Enter any string: '))
# for ch in s:
#     print(chr(ord(ch)+1))

# s = eval(input('Enter any string: '))
# s1=''
# for ch in s:
#     s1+=chr(ord(ch)+1)
# print(s1)

s = eval(input('Enter any string: '))
for ch in s:
    print(s.join[chr(ord(ch)+1)])