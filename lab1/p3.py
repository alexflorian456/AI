#!/usr/bin/env python3

n = int(input("nr linii: "))
m = int(input("nr coloane: "))
rez = 0

# vector 1
print("vector 1:")
v1 = []

for i in range(0,n):
	line = []
	for j in range(0,m):
		line.append(int(input("linia " + str(i+1) + " coloana " + str(j+1) + ": ")))
	v1.append(line)

# vector 2
print("vector 2:")

for i in range(0,n):
	for j in range(0,m):
		p=v1[i][j]*int(input("linia " + str(i+1) + " coloana " + str(j+1) + ": ")) #produsul dintre elementul din vectorul 1 si din vectorul 2
		if p!=0 : #adunam la suma doar daca p!=0
			rez = rez+p

print(rez)
