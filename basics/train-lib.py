#import math

#print(type(math))
#print(dir(math))

import math as m
import numpy as asarray

print(m.pi)

print(type(asarray))

rolls = asarray.random.randint(low=1, high=7, size=10)
print(type(rolls))
print(dir(rolls))

print(rolls.mean())

rolls = rolls + 10
print(rolls)

print(rolls <= 13)

xlist = [[1,2,3],[4,5,6]]

x = asarray.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

print(x[1,1])

print(False and (not False))


map = {"A": 11,"K":10,"J":10,"Q":10 }

print("A" in map)

for i in map:
    if("A" in map):
        print('n')
    print(i)