#How to create a python set
my_set = {1,2,3}
print(my_set)
my_set = {1.0, "Hello", (1,2,3)}
print(my_set)
my_set = set([1,2,3,2])
print(my_set)
#Modifying a set - add() - used to add a single element; update() - add multiple elements
my_set = {1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([3,4,5,6,7])
print(my_set)
#Removing elements from a set - discard() , remove() - raises error if element is  not present
my_set.discard(4)
print(my_set)
my_set.remove(7)
print(my_set)
print(my_set.pop())
my_set.clear()
print(my_set)
#Set Operations
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a|b)
print(a.union(b))
print(a & b)
print(a.intersection(b))
print(a-b)
print(a.difference(b))
print(b-a)
print(a ^ b) # set of elements in a and b but not in both (excluding the intersection)
