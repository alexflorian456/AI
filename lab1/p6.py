#!/usr/bin/env python3

n = int(input("nr de elemente: "))
d={} # dictionar pe post de vector de frecventa
maxim=0 # nr de aparitii al elementului cu cele mai multe aparitii
p=-1 # nr pe care il vom afisa

for i in range(0,n):
	x=int(input())
	if x in d:
		d[x]+=1
	else:
		d[x]=1 # daca nr citit se gaseste in vector, ii incrementam frecventa, daca nu, il adaugam
	if d[x]>maxim:
		maxim=d[x]
		p=x

if maxim>n/2:
	print("elementul majoritar este: "+str(p))
else:
	print("nu exista element majoritar")
