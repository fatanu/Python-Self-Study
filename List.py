from test.test_optparse import InterceptingOptionParser
my = list()
print(my)
ny = [1,2,3,4,5]
print(ny)
ny.append(6)
print(ny)
ny.extend([7,8,9])
print(ny)
print(ny + [10,11,12])
ny.insert(0, 0)
print(ny)
del ny[2]
print(ny)
print(ny.pop())
ny.remove(8)
print(ny)
print(ny.index(5))
print(ny.count(0))
print(ny)
ny.sort(reverse=True)
print(ny)
def myfunc(e):
    return len(e)
cars = ["Ford", "Mitsubishi", "BMW", "VW"]
cars.sort(reverse=True, key=myfunc)
print(cars)
ry = [0,1,2,4,5,6,7]
print(sorted(ry, reverse=True)) # sorted(iterable, key=jjjj, reverse=False)
ry.reverse()
print(ry)
