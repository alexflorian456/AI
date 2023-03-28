#!/usr/bin/env python3

import random

filename = input('introduceti un nume de fisier: ')
pop = int(input('introduceti populatia: '))
gen = int(input('introduceti numarul de generatii: '))

f = open(filename,'r')

n = int(f.readline())
print("n= " + str(n))

mat = []
for i in range(n):
    lmat = []
    for j in range(n):
        lmat.append(0)
    mat.append(lmat)

for i in range(n):
    line = f.readline().strip()
    if len(line.split()) != n:
        print("linia " + str(i) + " nu are " + str(n) +" elemente!")
    e = line.split()
    for j in range(n):
        mat[i][j] = e[j];

src = int(f.readline())
dest = int(f.readline())

print("src= "+str(src)+"\ndest= "+str(dest))

croms=[]
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

def init_pop():
    perm = [i for i in range(1,n+1)]
    perm.remove(src)
    perm.remove(dest)
    for i in range(pop):
        random.shuffle(perm)
        ind = perm.copy()
        ind.append(dest)
        ind.insert(0,src)
        fit = fitness(ind)
        print(str(ind) + " " + str(fit))
        croms.append(Chromosome(ind,fit))

def fitness(array):
    cost=0
    for i in range(1,n):
        cost += int(mat[array[i-1]-1][array[i]-1])
    return cost

def select_parent():
    pos1=random.randint(0,pop-1)
    pos2=random.randint(0,pop-1)
    if croms[pos1].getFitness() < croms[pos2].getFitness():
        return croms[pos1]
    else:
        return croms[pos2]

def crossover(c1, c2):
    repres1 = c1.getRepres().copy()
    repres2 = c2.getRepres().copy()
    repres1.remove(src)
    repres1.remove(dest)
    repres2.remove(src)
    repres2.remove(dest)
    pos1 = random.randint(0,n-3)
    pos2 = random.randint(0,n-3)
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    offspring = [0 for i in range(n-2)]
    for i in range(pos1, pos2):
        offspring[i] = repres2[i]
        repres1.remove(repres2[i])
    for i in range(pos2, n-2):
        offspring[i] = repres1.pop(0)
    for i in range(pos1):
        offspring[i] = repres1.pop(0)
    offspring.insert(0,src)
    offspring.append(dest)
    fit = fitness(offspring)
    return Chromosome(offspring,fit)

def mutate(crom):
    repres = crom.getRepres().copy()
    pos1 = random.randint(1,n-2)
    pos2 = random.randint(1,n-2)
    aux = repres[pos1]
    repres[pos1] = repres[pos2]
    repres[pos2] = aux
    crom.setRepres(repres)

init_pop()
globalMaxCrom = croms[0]
globalMaxCroms = [croms[0]]
for i in range(gen):
    new_croms=[]
    genCrom = croms[0]
    for j in range(pop):
        p1 = select_parent()
        p2 = select_parent()
        offspring = crossover(p1,p2)
        mutate(offspring)
        new_croms.append(offspring)
        if offspring.getFitness() < genCrom.getFitness():
            genCrom = offspring
        if offspring.getFitness() < globalMaxCrom.getFitness():
            globalMaxCroms = []
            globalMaxCrom = offspring
        if offspring.getFitness() == globalMaxCrom.getFitness():
            globalMaxCroms.append(offspring)
    croms = new_croms
    print("Generatia "+str(i+1)+" lungime drum minim: "+str(genCrom.getFitness()))

# Generam un numar de cicluri random care contin nodul dat.
# La functia de mutatie, verificam daca exista o muchie care
# "sare" peste un numar de noduri, in acest caz, eliminam aceste
# noduri din ciclu. Acest lucru il facem pentru a putea explora
# solutiile cu mai putine muchii.
# Vor avea fitness mai bun ciclurile de greutate mai mica.

print("Cele mai bune drumuri gasite: ")
for crom in globalMaxCroms:
    print(str(crom.getRepres())+" de lungime: "+str(crom.getFitness()))
