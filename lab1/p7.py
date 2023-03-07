#!/usr/bin/env python3

n = int(input("nr de elemente: "))
k = int(input("k= "))
v=[]

for i in range(0,n):
	v.append(int(input()))

v=list(set(v)) # eliminam elementele duplicate
v.sort(reverse=True)
print("al k-lea cel mai mare element din lista este: "+str(v[k-1]))
