# def factorial(n):
#     if n< 2:
#         return 1
#     return n * factorial(n-1)
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

def myfunc(e):
    return len(e)
cars = ["Ford", "Mitsubishi", "BMW", "VW"]
cars.sort(reverse=True, key=myfunc)
print(cars)
anuo = ("anuoluwapo", "fatokun")
print('-'.join((anuo)))
tise = "Anuoluwapo"
print(tise.strip())
mydict = {1:2, 2:4, 3:6, 4:8, 5:10}
print(mydict.popitem())
