#!/usr/bin/env python3

n=int(input("nr de linii: "))
m=int(input("nr de coloane: "))
mat=[[1,1,1,1,0,0,1,1,0,1],
	 [1,0,0,1,1,0,1,1,1,1],
	 [1,0,0,1,1,1,1,1,1,1],
	 [1,1,1,1,0,0,1,1,0,1],
	 [1,0,0,1,1,0,1,1,0,0],
	 [1,1,0,1,1,0,0,1,0,1],
	 [1,1,1,0,1,0,1,0,0,1],
	 [1,1,1,0,1,1,1,1,1,1]]

def bfs(i,j): #returneaza lista de coordonate care trebuie schimbate in 1, care pot fi accesate pornind din i,j
	bfs_list=[[i,j]]
	q=[]
	ok=True
	q.append([i,j])
	while len(q)>0:
		e=q.pop(0)
		x=e[0]
		y=e[1]

		#verificam daca zero-ul nostru face parte din acelasi grup cu un zero de pe margine, caz in care nu suntem pe o insula
		if mat[x-1][y]==0 and x-1==0:
			ok=False
			break
		if mat[x+1][y]==0 and x+1==n-1:
			ok=False
			break
		if mat[x][y-1]==0 and y-1==0:
			ok=False
			break
		if mat[x][y+1]==0 and y+1==m-1:
			ok=False
			break

		#adaugam vecinii 0 in coada si in lista
		if mat[x-1][y]==0 and [x-1,y] not in bfs_list:
			bfs_list.append([x-1,y])
			q.append([x-1,y])
		if mat[x+1][y]==0 and [x+1,y] not in bfs_list:
			bfs_list.append([x+1,y])
			q.append([x+1,y])
		if mat[x][y-1]==0 and [x,y-1] not in bfs_list:
			bfs_list.append([x,y-1])
			q.append([x,y-1])
		if mat[x][y+1]==0 and [x,y+1] not in bfs_list:
			bfs_list.append([x,y+1])
			q.append([x,y+1])

	if not ok:
		return []
	else:
		return bfs_list

#citim matricea
#for i in range(n):
#	lin = []
#	for j in range(m):
#		lin.append(int(input("linia "+str(i)+" coloana "+str(j)+": ")))
#	mat.append(lin)

#parcurgem elementele matricii, in afara de margini
for i in range(1,n-1):
	for j in range(1,m-1):
		bfs_list=bfs(i,j) # obtinem lista de coordonate de pe insula pe care se afla pozitia curenta, sau lista vida daca nu ne aflam pe o insula
		for coord in bfs_list:
			x=coord[0]
			y=coord[1]
			mat[x][y]=1

for i in range(n):
	string=""
	for j in range(m):
		string+=str(mat[i][j])+" "
	print(string)
