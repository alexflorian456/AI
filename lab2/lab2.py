#!/usr/bin/env python3

filename=input('introduceti un nume de fisier: ')
f = open(filename,'r')

n = int(f.readline())

mat = []
coms = []
edges = 0

for i in range(0,n):
	lmat = []
	for j in range(0,n):
		lmat.append(0)
	mat.append(lmat)
	coms.append([i+1])

line=f.readline().strip()
while line:
	e=line.split()
	x=int(e[0])-1
	y=int(e[1])-1
	mat[x][y]=1
	mat[y][x]=1
	edges+=1
	line=f.readline().strip()

#for i in range(0,n):
#	string=''
#	for j in range(0,n):
#		string+=str(mat[i][j])
#	print(string)

def compute_Q(communities):
	Q = 0
	for com in communities:
		k_u = 0
		m_u = 0
		for node in com:
			for j in range(0,n):
				k_u += mat[node-1][j]
				if j+1 in com:
					m_u += mat[node-1][j]
		m_u = m_u // 2
		Q += m_u/edges - (k_u/(2*edges))*(k_u/(2*edges))
	return Q

# initializam Q pentru cazul in care fiecare nod are comunitatea lui
Q = compute_Q(coms)
ok = True
while ok:
	ok = False
	maxcoms=coms.copy()
	for i in range(0,len(coms)-1):
		for j in range(i+1,len(coms)):
			tempcoms = []
			com1 = coms[i]
			com2 = coms[j]
			com_pair = com1 + com2
			tempcoms.append(com_pair)
			for k in range(0,len(coms)):
				if k!=i and k!=j:
					tempcoms.append(coms[k])
			tempQ = compute_Q(tempcoms)
			if tempQ > Q:
				Q = tempQ
				maxcoms = tempcoms
				ok = True
	coms=maxcoms

print("Q = "+str(Q))
print("nr de comunitati: "+str(len(coms)))
print("comunitati: "+str(coms))

community_idx=[]

for i in range(n):
    community_idx.append(0)

for i in range(len(coms)):
    for node in coms[i]:
        community_idx[node-1]=i+1

print("indecsi comunitati: "+str(community_idx))












