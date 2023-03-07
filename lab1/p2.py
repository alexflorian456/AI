#!/usr/bin/env python3
import math
print("introduceti perechi de coordonate separate prin spatiu: ")
p1 = input("perechea 1: ")
p2 = input("perechea 2: ")

t1 = tuple(int(item) for item in p1.split())
t2 = tuple(int(item) for item in p2.split())

x1 = t1[0]
y1 = t1[1]

x2 = t2[0]
y2 = t2[1]

print(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)))
