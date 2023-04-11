#!/usr/bin/env python3

from random import random, randint
import numpy as np
from math import sqrt
from numpy import matrix
from numpy import linalg
from sklearn import linear_model

v=input("(1,2,3): ")

print("folosing biblioteci specializate:")
v1 = open("lab6v"+v+".txt","r")

X = []
Y = []

line = v1.readline().strip()
line = v1.readline().strip()
while line:
    el = line.split(",")
    gdp_free = [float(el[5]),float(el[8])]
    X.append(gdp_free)
    Y.append(float(el[2]))
    line = v1.readline().strip()

regressor = linear_model.LinearRegression()
regressor.fit(X,Y)

w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
print("f(x1,x2) = ",w0," + ",w1,"*x1 + ",w2,"*x2")

if v=="1":
    print("folosind cod propriu:")
    
    Y = [ [el] for el in Y ]
    
    # X deocamdata este de forma
    # [[1,2],
    #  [3,4],
    #  [5,6]] prima coloana = GDP, a doua freedom
    # dar ar trebui sa fie
    # [[1,3,5],
    #  [2,4,6]]
    
    gdp = []
    free = []
    for line in X:
        gdp.append(line[0])
        free.append(line[1])
    
    X = [[1,el1,el2] for el1,el2 in zip(gdp,free)]
    XT = X.copy() # pastram X curent, care este de fapt transpusa lui X
    
    # il transpunem pe X pentru a-l obtine pe X
    
    X = []
    for i in range(3):
        l = []
        for j in range(len(XT)):
            l.append(XT[j][i])
        X.append(l)
    
    prod = []
    for i in range(len(X)):
        l = []
        for j in range(len(XT[0])):
            s = 0
            for k in range(len(XT)):
                s += X[i][k] * XT[k][j]
            l.append(s)
        prod.append(l)
    
    
    def zeros_matrix(rows, cols):
        A = []
        for i in range(rows):
            l = []
            for j in range(cols):
                l.append(0)
            A.append(l)
        return A
    
    def multiplyMatrices(matrix1, matrix2): 
         res = zeros_matrix(len(matrix1), len(matrix2[0])) 
         for i in range(len(matrix1)): 
             for j in range(len(matrix2[0])): 
                 for k in range(len(matrix2)): 
                     res[i][j] += matrix1[i][k] * matrix2[k][j] 
         return res
    
    def copyMatrix(M):
        rows = len(M)
        cols = len(M[0])
    
        MC = zeros_matrix(rows, cols)
    
        for i in range(rows):
            for j in range(rows):
                MC[i][j] = M[i][j]
    
        return MC
    
    def getIdentityMatrix(rows,cols):
        I = []
        for i in range(rows):
            l = []
            for j in range(cols):
                if i==j:
                    l.append(1)
                else:
                    l.append(0)
            I.append(l)
        return I
    
    def invertMatrix(matrix): 
        mc = copyMatrix(matrix) 
        im = getIdentityMatrix(len(matrix), len(matrix[0])) 
        imc = copyMatrix(im) 
        indices = list(range(len(matrix))) 
        for fd in range(len(matrix)): 
            fdScaler = 1 / mc[fd][fd] 
            for j in range(len(matrix)): 
                mc[fd][j] *= fdScaler 
                imc[fd][j] *= fdScaler 
            for i in indices[0:fd] + indices[fd + 1:]: 
                crScaler = mc[i][fd] 
                for j in range(len(matrix)): 
                    mc[i][j] = mc[i][j] - crScaler * mc[fd][j] 
                    imc[i][j] = imc[i][j] - crScaler * imc[fd][j] 
        return imc

    inv_prod = invertMatrix(prod)

    prod = []
    for i in range(len(inv_prod)):
        l = []
        for j in range(len(X[0])):
            s = 0
            for k in range(len(X)):
                s += inv_prod[i][k] * X[k][j]
            l.append(s)
        prod.append(l)
    
    W = []
    for i in range(len(prod)):
        l = []
        for j in range(len(Y[0])):
            s = 0
            for k in range(len(Y)):
                s += prod[i][k] * Y[k][j]
            l.append(s)
        W.append(l)
    
    print("f(x1,x2) = ",W[0][0]," + ",W[1][0],"*x1 + ",W[2][0],"*x2")
    RMSE=0
    for i in range(len(XT)):
        yComp = W[0][0] + W[1][0]*XT[i][1] + W[2][0]*XT[i][2]
        dif = (yComp - Y[i][0])**2
        RMSE += dif
    RMSE /= len(XT)
    RMSE = sqrt(RMSE)
    print("Error: ",RMSE)
else:
    RMSE=0
    for i in range(len(X)):
        yComp = w0 + w1*X[i][0] + w2*X[i][1]
        dif = (yComp - Y[i])**2
        RMSE += dif
    RMSE /= len(X)
    RMSE = sqrt(RMSE)
    print("Error: ",RMSE)
    
