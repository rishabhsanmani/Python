# s = {10,20,30,'python','java',10}
# print(fs)
# print(type(fs))
# print(id(fs))
# print(len(fs))
# print(max(fs))
# print(min(fs))
# print(sum(fs))


s = {1,2,3,4,5}
fs = frozenset(s)
t = {2,4,6,8,10}
r = {2,4}
a = {9,6,8,7}

# a = fs.union(t)
# print(a)

# print(fs.intersection(t))
# print(t.intersection(fs))


# print(fs.difference(t))
# print(t.difference(fs))

# print(fs.symmetric_difference(t))
# print(t.symmetric_difference(fs))

print(fs.issubset(r))
print(r.issubset(fs))

print(fs.issuperset(r))
print(r.issuperset(fs))

print(fs.isdisjoint(a))