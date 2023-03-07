#!/usr/bin/env python3

frecv = {} #dictionar pe post de vector de frecventa
text = input("text: ")
words = text.split()

for word in words:
	if word in frecv:
		frecv[word]+=1
	else:
		frecv[word]=1

for key,value in frecv.items():
	if value==1:
		print(key)
