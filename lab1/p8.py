#!/usr/bin/env python3

n=int(input("introduceti un numar: "))

def binary(n):
	binar=""
	while n>0: # transformam numarul in reprezentarea sa binara folosind resturile impartirii sale repetate la 2
		binar=str(n%2)+binar
		n=n//2
	return binar

for i in range(1,n+1):
	print(binary(i))
