#!/usr/bin/env python3

n = int(input("nr linii: "))
m = int(input("nr coloane: "))
p = int(input("nr submatrici: "))
print("Introduceti matricea:")
mat=[]
sm=[]

for i in range(0,n): # citim matricea
	l=[]
	for j in range(0,m):
		l.append(int(input("linia "+str(i)+" coloana "+str(j)+": ")))
	mat.append(l)

print("Introduceti submatrici (perechi separate prin virgula):")

for i in range(0,p): # citim perechile de coordonate ale colturilor submatricilor
	print("submatricea "+ str(i+1))
	per=[]
	s1 = input("perechea 1: ")
	p1 = s1.split(",")
	p1[0] = int(p1[0])
	p1[1] = int(p1[1])
	s2 = input("perechea 2: ")
	p2 = s2.split(",")
	p2[0] = int(p2[0])
	p2[1] = int(p2[1])
	per.append(p1)
	per.append(p2)
	sm.append(per)

for per in sm:
	s=0
	x1=per[0][0]
	y1=per[0][1]
	x2=per[1][0]
	y2=per[1][1]
	for i in range(x1,x2+1): # parcurgem submatricea delimitata de coordonate
		for j in range(y1,y2+1):
			s+=mat[i][j]
	print("suma submatricei def de " + str(per) + " este: " + str(s))		
