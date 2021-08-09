x = {1,2,3,4,5}

z = frozenset(x)
print(type(z))

#We can add frozenset in set
x.add(z)
print(x)
