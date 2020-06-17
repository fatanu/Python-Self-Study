my_dict = {}
print(my_dict)
#my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)
#Accessing elements from dictionary
print(my_dict[1])
print(my_dict.get(2))
print(my_dict.get(3, "anu"))
#Changing and Adding Dictionary Elements
my_dict['age'] = 32
print(my_dict)
my_dict[1] = 'mango'
print(my_dict)
#Removing elements from Dictionary
print(my_dict.pop('age'))
print(my_dict.popitem())
print(my_dict)
my_dict.clear()
print(my_dict)
#DIctionary fromkeys()
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)
val = [1]
vowels = dict.fromkeys(keys, val)
print(vowels)
val.append(2)
print(vowels)
vall = [3]
ola = {key : vall for key in keys}
print(ola)
#items() - returns a view obj that deisplays a list of dict's key/value tuple pairs
print(ola.items())
#keys() - Returns a view object that displays a list of all the keys in the dictionary
print(ola.keys())
#setdefault() - retunrs the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
print(ola.setdefault('a'))
print(ola.setdefault('f', 89))
print(ola)
#pop() - return value of the specified key if found and if not default value supply
print(ola.pop('a'))
print(ola.pop('g', 57))
print(ola)
#values() - returns a view object that displays a list of all the values in the dict
print(ola.values())
#update() - updates the dictionary with the elements from another dictionary obj or from an iterable of key/value pairs
d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)

d1 = {3: "three"}
d.update(d1)
print(d)
fruits = {'mango': 100, 'Orange':200}
sm = 0
for v in list(fruits.values()):
    sm += v
print(sm)
if "Guava" in list(fruits.keys()):
    print("Yes there is a guava")
else: print("There is no Guava")
print(list(fruits.keys()))
d4 = {'x': 2}

d4.update(y = 3, z = 0)
print(d4)