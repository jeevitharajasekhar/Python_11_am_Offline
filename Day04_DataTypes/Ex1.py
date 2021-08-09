#Set contains unordered elements, Insertion order not preserved
s = { 10, 20, 30, 40, 50, 10, 20}
print(s)
print(type(s))

#Performing Update in set, we cannot expect exact index`s in set
s = { 10, 20, 30, 40, 50, 10, 20}
s.update({60, 70})
print(s)

#Remove the elements
s = {1,2,3,4,5}
s.remove(3)
#s.remove(6) #KeyError: 6
print(s) #{1, 2, 4, 5}

#Adding the values in set
s = {1,2}
s.add(3)
s.add(4)
s.add(5)
print(s) #{1, 2, 3, 4, 5}

#Index Calls
s = {10,20,30,40,50}
#print(s[1]) #TypeError: 'set' object is not subscriptable

#print(s[0:5]) #TypeError: 'set' object is not subscriptable

print(s*2) #TypeError: unsupported operand type(s) for *: 'set' and 'int'







