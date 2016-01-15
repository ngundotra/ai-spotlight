# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:11:05 2016

@author: codetesting
"""

import numpy as np
import matplotlib.pyplot as plt

def convertToBoolean(string):
    booleanList = []
    for x in string:
        if x == "0":
            booleanList.append(False)
        else:
            booleanList.append(True)
    return tuple(booleanList)
    
rules = ("111", "110", "101", "100", "011", "010", "001", "000")

rulesBool = []
for string in rules:
    rulesBool.append(convertToBoolean(string))

class CellAuto():
    rulesBool = tuple(rulesBool)
    
    def __init__(self, elements=10, iterations=15, rule=110):
        self.elements = elements
        self.iterations = iterations
        self.rule = rule
        self.history = []
        self.convertRule()
        
    def nextLine(self,elementRow=[]):
        if not elementRow:
            elementRow = np.random.choice([True, False], self.elements, p=[0.4, 0.6]).astype(list)
            elementRow = list(elementRow)
        nextElementRow = []
        for element in range(len(elementRow)):
            neighbors = []
            for index in range(-1,2):
                choice = (index+element)%len(elementRow)
                neighbors.append(elementRow[choice])
            nextElementRow.append(self.ruleTable[tuple(neighbors)])
        return nextElementRow
        
    def convertRule(self):
        num = self.rule
        ruleBool = []
        for i in [2**x for x in range(7,-1,-1)]:
            if num - i >= 0:
                ruleBool.append(True)
                num = num - i
            else:
                ruleBool.append(False)
        self.ruleInBool = ruleBool
        self.ruleTable = {rulesBool[x]:ruleBool[x] for x in range(8)}
        
    def run(self, elementRow=[]):
        self.history.append(elementRow)
        for x in range(self.iterations-1):
            elementRow = self.nextLine(elementRow)
            self.history.append(elementRow)
            
    def writeToFile(self, filename="rule110.txt"):
        filename = "rule" + str(self.rule) + ".txt"
        f = open(filename, "w+")
        for line in self.history:
            for element in line:
                if element:
                    f.write("1")
                else:
                    f.write("0")
            f.write("\n")
        f.close()
        
    def display(self):
        bool2num = []
        for line in self.history:
            for element in line:
                if element:
                    bool2num.append(255)
                else:
                    bool2num.append(0)
        boolArray = np.reshape(np.array(bool2num), (self.iterations, self.elements))
        plt.matshow(boolArray)
        return plt
     
rule110 = CellAuto(elements=100,iterations=27,rule=90)
rule110.run([True if x == (rule110.elements/2-1) else False for x in range(rule110.elements)])
myplot = rule110.display()
myplot.savefig("rule90.pdf",bbox_inches='tight')

        