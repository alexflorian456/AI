#!/usr/bin/env python3

n = int(input("nr de elemente: "))
d = {} # dictionar pe post de vector de frecventa
p = -1 # nr pe care il vom afisa

for i in range(0,n):
	x = int(input())
	if x in d:
		p=x # daca nr citit se gaseste deja in dictionar, p=x
	else:
		d[x]=0 # daca nu, il adaugam in dictionar pentru a folosi aceasta informatie in viitorii pasi

print("elementul care se repeta este "+str(p))
	
