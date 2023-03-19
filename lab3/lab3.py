#!/usr/bin/env python3

import random

# un cromozom reprezinta o impartire in comunitati
# de ex. pentru n=3 norduri un cromozom posibil este [1,2,1],
# adica nodurile 1 si 3 fac parte din comunitatea 1,
# iar nodul 2 din comunitatea 2

filename = input('introduceti un nume de fisier: ')
pop = int(input('introduceti populatia: '))
gen = int(input('introduceti numarul de generatii: '))

f = open(filename,'r')

n = int(f.readline())

class Chromosome:
    def __init__(self,repres,fitness):
        self.__repres=repres
        self.__fitness=fitness

    def getRepres(self):
        return self.__repres

    def getFitness(self):
        return self.__fitness

    def setRepres(self,nRepres):
        self.__repres=nRepres

    def setFitness(self,nFitness):
        self.__fitness=nFitness


mat = [] # matrice de adiacenta
edges = 0 # nr de muchii
croms = [] # populatia de indivizi

# initializare matrice de adiacenta (folosita la calculul modularitatii)
for i in range(0,n):
	lmat = []
	for j in range(0,n):
		lmat.append(0)
	mat.append(lmat)
line=f.readline().strip()
while line:
	e=line.split()
	x=int(e[0])-1
	y=int(e[1])-1
	mat[x][y]=1
	mat[y][x]=1
	edges+=1
	line=f.readline().strip()

# initializeaza populatia initiala
def init_pop():
    for i in range(pop):
        crom=[]
        for j in range(n):
            crom.append(random.randint(1,n))
        coms=crom_to_coms(crom)
        fitness=compute_Q(coms)
        chromosome=Chromosome(crom,fitness)
        croms.append(chromosome)

# transforma un cromozom intr-o lista de comunitati
def crom_to_coms(crom):
    coms=[]
    dict_coms={}
    for i in range(n):
        if crom[i] in dict_coms:
            dict_coms[crom[i]].append(i+1)
        else:
            dict_coms[crom[i]]=[i+1]
    for key, value in dict_coms.items():
        coms.append(value)
    return coms

# evalueaza modularitatea unei liste de comunitati
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

# selecteaza un parinte
def select_parent(population):
    pos1=random.randint(0,pop-1)
    pos2=random.randint(0,pop-1)
    if population[pos1].getFitness() > population[pos2].getFitness():
        return population[pos1]
    else:
        return population[pos2]

# incruciseaza doi cromozomi
def crossover(p1,p2):
    offspringR=[]
    jum=n//2
    repres1=p1.getRepres()
    repres2=p2.getRepres()
    for i in range(n):
        if i <= jum:
            offspringR.append(repres1[i])
        else:
            offspringR.append(repres2[i])
    offspring_coms = crom_to_coms(offspringR)
    fitness = compute_Q(offspring_coms)
    offspring = Chromosome(offspringR,fitness)
    return offspring

# genereaza o mutatie in genomul unui cromozom
def mutate(crom):
    mutation=random.randint(1,n)
    mutation_pos=random.randint(0,n-1)
    repres=crom.getRepres()
    repres[mutation_pos]=mutation
    crom.setRepres(repres)

init_pop()

#for crom in croms:
#    print(crom.getRepres())
#    print(crom_to_coms(crom.getRepres()))

for i in range(gen):
    new_croms=[]
    l=0
    while l<pop:
        p1=select_parent(croms)
        p2=select_parent(croms)
        offspring=crossover(p1,p2)
        mutate(offspring)
        new_croms.append(offspring)
        l+=1
    croms=new_croms

maxQ=compute_Q(crom_to_coms(croms[0].getRepres()))
maxCrom=croms[0]
for crom in croms:
    Q=compute_Q(crom_to_coms(crom.getRepres()))
    if Q>maxQ:
        maxQ=Q
        maxCrom=crom

print('Cromozomul final: ' + str(maxCrom.getRepres()))
print('Modularitate: ' + str(maxQ))
print('Impartirea in comunitati: ' + str(crom_to_coms(maxCrom.getRepres())))
