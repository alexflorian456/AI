#!/usr/bin/env python3
import csv
import numpy as np
import random

data = []
dataNames = []
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            dataNames = row
        else:
            data.append(row)
        line_count += 1
GDPvar = dataNames.index("Economy..GDP.per.Capita.")
GDP = [float(data[i][GDPvar]) for i in range(len(data))]
Freevar = dataNames.index("Freedom")
Freedom = [float(data[i][Freevar]) for i in range(len(data))]
Happyvar = dataNames.index("Happiness.Score")
Happiness = [float(data[i][Happyvar]) for i in range(len(data))]

# normalizare date
minGDP = min(GDP)
maxGDP = max(GDP)
normGDP = [(gdp-minGDP)/(maxGDP-minGDP) for gdp in GDP]

minFree = min(Freedom)
maxFree = max(Freedom)
normFree = [(free-minFree)/(maxFree-minFree) for free in Freedom]

minHappy = min(Happiness)
maxHappy = max(Happiness)
normHappy = [(happy-minHappy)/(maxHappy-minHappy) for happy in Happiness]

GDP = normGDP
Freedom = normFree
Happiness = normHappy

# folosind tool
print("tool:")
from sklearn import linear_model
regressor = linear_model.SGDRegressor()
inputs = []
for i in range(len(GDP)):
    inputs.append([GDP[i],Freedom[i]])
regressor.fit(inputs,Happiness)
w0,w1,w2 =  regressor.intercept_,regressor.coef_[0],regressor.coef_[1]
print('f(x) = ', w0[0], ' + ', w1, ' * x1 + ', w2, ' * x2' )
indexes = random.sample(range(len(inputs)),50)
testInputs = [inputs[idx] for idx in indexes]
testOutputs = [Happiness[idx] for idx in indexes]
computedTestOutputs = []
for input_ in testInputs:
    computedTestOutputs.append(w0 + w1*input_[0] + w2*input_[1])
from sklearn.metrics import mean_squared_error

error = mean_squared_error(testOutputs, computedTestOutputs)
print('prediction error:  ', error)

# folosind cod propriu

class MBGDRegressor:
    def __init__(self,batch_size,learning_rate=0.01,epochs=100):
 
        self.coef_ = None
        self.intercept_ = None
        self.lr = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
    def fit(self,X_train,y_train):
        self.intercept_ = 0
        self.coef_ = np.ones(X_train.shape[1])
        
        for i in range(self.epochs):
            for j in range(int(X_train.shape[0]/self.batch_size)):
                
                idx = random.sample(range(X_train.shape[0]),self.batch_size)

                y_hat = np.dot(X_train[idx],self.coef_) + self.intercept_
                intercept_der = -2 * np.mean(y_train[idx] - y_hat)
                self.intercept_ = self.intercept_ - (self.lr * intercept_der)
                coef_der = -2 * np.dot((y_train[idx] - y_hat),X_train[idx])
                self.coef_ = self.coef_ - (self.lr * coef_der)    
        #print(self.intercept_,self.coef_)
    
    def predict(self,X_test):
        return np.dot(X_test,self.coef_) + self.intercept_

regressor = MBGDRegressor(10)
inputNdArray = np.array(inputs)
outputNdArray = np.array(Happiness)
regressor.fit(inputNdArray,outputNdArray)
print("cod propriu:")
print("multivariata:")
print('f(x) = ', regressor.intercept_, ' + ', regressor.coef_[0], ' * x1 + ', regressor.coef_[1], ' * x2' )
indexes = random.sample(range(len(inputs)),50)
testInputs = [inputs[idx] for idx in indexes]
testOutputs = [Happiness[idx] for idx in indexes]
computedTestOutputs = []
for input_ in testInputs:
    computedTestOutputs.append(regressor.intercept_ + regressor.coef_[0]*input_[0] + regressor.coef_[1]*input_[1])
error = 0.0
for t1, t2 in zip(computedTestOutputs, testOutputs):
    error += (t1 - t2) ** 2
error = error / len(testOutputs)
print('prediction error: ', error)

inputNdArray = np.array([[inputs[i][0]] for i in range(len(inputs))])
print("univariata:")
regressor.fit(inputNdArray,outputNdArray)
print('f(x) = ', regressor.intercept_, ' + ', regressor.coef_[0],
 ' * x1')

indexes = random.sample(range(len(inputs)),50)
testInputs = [inputs[idx] for idx in indexes]
testOutputs = [Happiness[idx] for idx in indexes]
computedTestOutputs = []
for input_ in testInputs:
    computedTestOutputs.append(regressor.intercept_ + regressor.coef_[0]*input_[0])# + regressor.coef_[1]*input_[1])
error = 0.0
for t1, t2 in zip(computedTestOutputs, testOutputs):
    error += (t1 - t2) ** 2
error = error / len(testOutputs)
print('prediction error: ', error)
