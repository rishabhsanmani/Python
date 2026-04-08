# collection of 'key''value' pairs
# inclosed by {}
# pairs are seperated by comma
# key values seperated by colon (:)
# * key must be unique
# * value may be duplicate
# * indexing not supported
# * slicing not supported
# mutable in nature

# --------------python function------------------

# d = {'name':'Neeraj','age':37,'quali':'M.Tech'}
# a = {1:'Neeraj',2:37,3:'M.Tech'}
# b= {1:'Neeraj',2:37,'3':'M.Tech'}
# print(d)
# print(type(d))
# print(len(d))
# print(max(d))
# print(min(d))
# print(sum(a))
# print(sum(b))


# ---------------dictionary method---------------

# copy() :- create new object
# clear() :- remove all pairs feom dict
# get() :- d.get('key') -> 'value'
# keys() :- returns all the keys
# values() :- return all the values
# items() :- return the pair of key and value
# fromkeys() :- 
# updated() :-
# setdefault() :-
# pop() :-
# popitem() :-



d = {'name': 'Rishabh','age':19,'course':'FSD'}
# d1 = d.copy()
# print(d)
# print(id(d1),id(d))

# d.clear()
# print(d)

# print(d.get('name'))

# print(d.keys())

# print(d.values())

# print(d.items())

# a={}
# l=[1,2,3,4]
# print(a.fromkeys(l))

# d.update({'city':'Chhindwara', 'contact_no':3666985485})
# print(d)

# d.update({'city':'Chhindwara'})
# print(d)

# d.pop('age')
# print(d)

# d.popitem()
# print(d)