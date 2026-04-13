# set => 
# collection of unique element
# enclosed with {} and seperated by (,)
# unordered collection
# indexing not supported
# slicing not supported
# mutable in nature

# ------------------Python Inbuilt Function------------------------------------

# s = {10,20,30,'python','java',10}
# print(s)
# print(type(s))
# print(id(s))
# print(len(s))
# print(max(s))
# print(min(s))
# print(sum(s))


# --------------------Set Method------------------------------------------------

# methods for 2 or more than 2 set
# 1. union()                      ---------
# 2. intersection()                       |
#                                         |       give new set
# 3. differences()                        |
# 4. symatic-difference()         ---------
# 5. intersation_update()         ---------
# 6. differences_update()                 |       
# 7. symatic-difference_update()  ---------
# 8. issubset()                      ------
#                                         |      boolean
# 9. issuperset()                    ------



# s = {1,2,3,4,5}
# t = {2,4,6,8,10}
# r = {2,4}
# a = {9,6,8,7}

# print(s.union(t))

# print(s.intersection(t))
# print(t.intersection(s))


# print(s.difference(t))
# print(t.difference(s))

# print(s.symmetric_difference(t))
# print(t.symmetric_difference(s))

# s.intersection_update(t)
# print(s)

# s.difference_update(t)
# print(s)

# s.symmetric_difference_update(t)
# print(s)

# print(s.issubset(r))
# print(r.issubset(s))

# print(s.issuperset(r))
# print(r.issuperset(s))

# print(s.isdisjoint(a))

# -------------------Methods works on single set----------------------------

# 1. add() :- to add single element at random position
# 2. update() :- to add multiple elements in random position

# 3. remove(element) :- remove element
# 4. discard() :- same as remove but it didn't give erroe if element is not present in set 

# 5. pop() :- to remove random element
# 6. clear() :- 
# 7. copy() :- 


s = {'python',10,20,'java'}

# s.add(50)
# print(s)

# s.update({90,60})
# print(s)
# s.update({'python',90})
# print(s)
# s.update({'pyhton'})
# print(s)

# s.remove('python')
# print(s)
# s.remove('python')
# print(s)

# s.discard('php')
# print(s)
# s.discard('java')
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)

# del s
# print(s)

# p=s.copy()
# print(p,s)
# print(id(p),id(s))
