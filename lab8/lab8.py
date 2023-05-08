#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
classifier = linear_model.LogisticRegression()
data = load_iris()
inputs = data['data']
outputs = data['target']
scaler.fit(inputs)
normInputs = scaler.transform(inputs)

classifier.fit(normInputs,outputs)

w0 = [classifier.intercept_[_] for _ in range(3)]
w1 = [classifier.coef_[_][0] for _ in range(3)]
w2 = [classifier.coef_[_][1] for _ in range(3)]
w3 = [classifier.coef_[_][2] for _ in range(3)]
w4 = [classifier.coef_[_][3] for _ in range(3)]

print("folosind tool:")
print("f1(x,y,z,t) = ",w0[0]," + ",w1[0],"*x + ",w2[0],"*y + ",w3[0],"*z + ",w4[0],"*t")
print("f2(x,y,z,t) = ",w0[1]," + ",w1[1],"*x + ",w2[1],"*y + ",w3[1],"*z + ",w4[1],"*t")
print("f3(x,y,z,t) = ",w0[2]," + ",w1[2],"*x + ",w2[2],"*y + ",w3[2],"*z + ",w4[2],"*t")

from sklearn.metrics import accuracy_score
computedOutputs = classifier.predict(normInputs)
error = 1 - accuracy_score(outputs,computedOutputs)
print("eroare (tool):",error)
print("acuratete (tool):",1-error)

from math import exp
from numpy.linalg import inv
import numpy as np

def sigmoid(x):
    return 1 / (1 + exp(-x))
    
class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learningRate = 0.001, noEpochs = 1000):
        self.coef_ = [0.0 for _ in range(1 + len(x[0]))]    
        for epoch in range(noEpochs):
            for i in range(len(x)): 
                ycomputed = sigmoid(self.eval(x[i], self.coef_))
                crtError = ycomputed - y[i]
                for j in range(0, len(x[0])):
                    self.coef_[j + 1] = self.coef_[j + 1] - learningRate * crtError * x[i][j]
                self.coef_[0] = self.coef_[0] - learningRate * crtError * 1
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
 
    def eval(self, xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predictOneSample(self, sampleFeatures):
        threshold = 0.5
        coefficients = [self.intercept_] + [c for c in self.coef_]
        computedFloatValue = self.eval(sampleFeatures, coefficients)
        computed01Value = sigmoid(computedFloatValue)
        computedLabel = 0 if computed01Value < threshold else 1 
        return computedLabel

    def predict(self, inTest):
        computedLabels = [self.predictOneSample(sample) for sample in inTest]
        return computedLabels

label1out = [1 if el == 0 else 0 for el in outputs]
label2out = [1 if el == 1 else 0 for el in outputs]
label3out = [1 if el == 2 else 0 for el in outputs]

label1cl = MyLogisticRegression()
label2cl = MyLogisticRegression()
label3cl = MyLogisticRegression()

label1cl.fit(normInputs,label1out)
label2cl.fit(normInputs,label2out)
label3cl.fit(normInputs,label3out)

print("folosind cod propriu:")
print("f1(x,y,z,t) = ",
        label1cl.intercept_," + ",
        label1cl.coef_[0],"*x + ",
        label1cl.coef_[1],"*y + ",
        label1cl.coef_[2],"*z + ",
        label1cl.coef_[3],"*t")
print("f2(x,y,z,t) = ",
        label2cl.intercept_," + ",
        label2cl.coef_[0],"*x + ",
        label2cl.coef_[1],"*y + ",
        label2cl.coef_[2],"*z + ",
        label2cl.coef_[3],"*t")
print("f3(x,y,z,t) = ",
        label3cl.intercept_," + ",
        label3cl.coef_[0],"*x + ",
        label3cl.coef_[1],"*y + ",
        label3cl.coef_[2],"*z + ",
        label3cl.coef_[3],"*t")

label1pred = label1cl.predict(normInputs)
label2pred = label2cl.predict(normInputs)
label3pred = label3cl.predict(normInputs)

computedOutputs = []
for i in range(len(label1pred)):
    ok = False
    if label1pred[i]==1:
        computedOutputs.append(0)
        ok = True
        continue
    if label2pred[i]==1:
        computedOutputs.append(1)
        ok = True
        continue
    if label3pred[i]==1:
        computedOutputs.append(2)
        ok = True
        continue
    if not ok:
        computedOutputs.append(0)

error = 0.0
for t1, t2 in zip(computedOutputs, outputs):
    if (t1 != t2):
        error += 1
error = error / len(outputs)
accuracy = 1 - error
print("eroare (cod propriu): ", error)
print("acuratete (cod propriu): ",accuracy)
