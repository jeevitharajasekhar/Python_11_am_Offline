#Slicing
#Syntax
#String [start/begin : end(-1) : stepOver(default value is 1)
lst = [1,2,3,4,5,6,7,8,9]
#      0,1,2,3,4,5,6,7,8
print(lst[3:6]) #[4, 5, 6]

#Beign is optional : (end-1)
print(lst[ : 3]) #[1, 2, 3]

#End is optional
print(lst[2:])

print(lst[ : ]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

