x = {1,2,3,4,5}
print(type(x)) #<class 'set'>

y = frozenset(x)
print(type(y)) #<class 'frozenset'>

# y.add(6)
# print(y) #AttributeError: 'frozenset' object has no attribute 'add'

y.remove(4)
print(y) #AttributeError: 'frozenset' object has no attribute 'remove'

