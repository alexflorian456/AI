#!/usr/bin/env python3
string = input("introduceti o propozitie: ")
words = string.split(" ")
# algoritmul de maxim pe cuvinte
lastword = ""
for word in words:
	if word>lastword:
		lastword=word

print(lastword)
