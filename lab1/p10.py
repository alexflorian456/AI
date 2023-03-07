#!/usr/bin/env python3

n=int(input("nr linii: "))
m=int(input("nr coloane: "))
minim=m+1 # ni se cere linia cu cel mai multe cifre 1 => cele mai putine cifre 0
linie=-1 # nr de linie pe care il vom afisa

for i in range(0,n):
	for j in range(0,m):
		x=int(input("linia "+str(i)+" coloana "+str(j)+": ")) # citim matricea
		if x==1 and j<minim: # daca am dat de un 1, inseamna ca j = nr de cifre 0
			linie=i
			minim=j

print("linia cu cele mai multe cifre de 1 este: "+str(linie+1))	
