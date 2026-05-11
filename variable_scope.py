# category of variable scope
# 1. Local variable :-
# 2. Global variable :-
# 3. non-local variable :-

# we can access local variable with global keyword




# def add():
#     global x
#     x=10
#     print(x)
# add()
# print(x)

x=10
def add():
    x=50
    print(x)
    print(globals()['x'])
add()
# print(x)