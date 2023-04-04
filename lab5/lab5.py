#!/usr/bin/env python3
from math import sqrt,log
sport = open("sport.csv","r")
flowers = open("flowers.csv","r")

pbin = open("prob-bin.txt")
tbin = open("true-bin.txt")

binsamples = 0
binsum = 0
print("Loss clasificare binara:")
line1 = pbin.readline().strip()
line2 = tbin.readline().strip()
while line1:
    binsamples += 1
    predicted = float(line1.split()[0])
    real = float(line2.split()[1])
    binsum += real * log(predicted) + (1 - real) * log(1-predicted)
    line1 = pbin.readline().strip()
    line2 = tbin.readline().strip()

print((-1/binsamples)*binsum)

pmc = open("prob-mc.txt")
tmc = open("true-mc.txt")

mcsamples = 0
mcsum0 = 0
mcsum1 = 0
mcsum2 = 0
print("Loss clasificare multi-clasa:")
line1 = pmc.readline().strip()
line2 = tmc.readline().strip()
while line1:
    mcsamples += 1
    probs = line1.split()
    p0 = float(probs[0])
    p1 = float(probs[1])
    p2 = float(probs[2])
    true = line2.split()
    t0 = float(true[0])
    t1 = float(true[1])
    t2 = float(true[2])
    
    mcsum0 += t0 * log(p0)
    mcsum1 += t1 * log(p1)
    mcsum2 += t2 * log(p2)
    
    line1 = pmc.readline().strip()
    line2 = tmc.readline().strip()

print((-1/mcsamples)*(mcsum0+mcsum1+mcsum2))

pmt = open("prob-mt.txt")
tmt = open("true-mt.txt")

mtsamples = 0
mtsum0 = 0
mtsum1 = 0
mtsum2 = 0
mtsum3 = 0
mtsum4 = 0

print("Loss clasificare multi-target:")
line1 = pmt.readline().strip()
line2 = tmt.readline().strip()

while line1:
    mtsamples += 1
    probs = line1.split()
    p0 = float(probs[0])
    p1 = float(probs[1])
    p2 = float(probs[2])
    p3 = float(probs[3])
    p4 = float(probs[4])

    true = line2.split()
    t0 = float(true[0])
    t1 = float(true[1])
    t2 = float(true[2])
    t3 = float(true[3])
    t4 = float(true[4])

    mtsum0 += t0 * log(p0)
    mtsum1 += t1 * log(p1)
    mtsum2 += t2 * log(p2)
    mtsum3 += t3 * log(p3)
    mtsum4 += t4 * log(p4)

    line1 = pmt.readline().strip()
    line2 = tmt.readline().strip()

print((-1/mtsamples)*(mtsum0+mtsum1+mtsum2+mtsum3+mtsum4))

weightErr1 = 0
waistErr1 = 0
pulseErr1 = 0
weightErr2 = 0
waistErr2 = 0
pulseErr2 = 0
sportsamples = 0

line = sport.readline().strip()
while line:
    sportsamples += 1
    vals = line.split(",")
    weight = int(vals[0])
    waist = int(vals[1])
    pulse = int(vals[2])
    Pweight = int(vals[3])
    Pwaist = int(vals[4])
    Ppulse = int(vals[5])

    weightErr1 += abs(Pweight - weight)
    waistErr1 += abs(Pwaist - waist)
    pulseErr1 += abs(Ppulse - pulse)

    weightErr2 += (Pweight - weight)**2
    waistErr2 += (Pwaist - waist)**2
    pulseErr2 += (Ppulse - pulse)**2

    line = sport.readline().strip()

weightErr1 /= sportsamples
waistErr1 /= sportsamples
pulseErr1 /= sportsamples

loss = (1/sportsamples) * (weightErr2 + waistErr2 + pulseErr2)

weightErr2 /= sportsamples
waistErr2 /= sportsamples
pulseErr2 /= sportsamples


weightErr2 = sqrt(weightErr2) 
waistErr2 = sqrt(waistErr2) 
pulseErr2 = sqrt(pulseErr2) 

print("SPORT:")
print("loss: "+str(loss))
print("weight err:")
print("L1: " + str(weightErr1))
print("L2: " + str(weightErr2))

print("waist err:")
print("L1: " + str(waistErr1))
print("L2: " + str(waistErr2))

print("pulse err:")
print("L1: " + str(pulseErr1))
print("L2: " + str(pulseErr2))

true = []
pred = []

line = flowers.readline().strip()
while line:
    vals = line.split(",")
    true.append(vals[0])
    pred.append(vals[1])
    line = flowers.readline().strip()

flowersamples = len(true)
correct = sum(1 for i in range(flowersamples) if true[i] == pred[i])
acc = correct/flowersamples
print("FLOWERS:")
print("accuracy: "+str(acc))

classes = ["Tulip","Daisy","Rose"]
for c in classes:
    TP = sum(1 for i in range(flowersamples) if true[i] == c and pred[i] == c)
    FP = sum(1 for i in range(flowersamples) if true[i] != c and pred[i] == c)
    FN = sum(1 for i in range(flowersamples) if true[i] == c and pred[i] != c)
    prec = TP / (TP + FP)
    rec = TP / (TP + FN)
    print(c+": ")
    print("precision: "+str(prec))
    print("recall: "+str(rec))
