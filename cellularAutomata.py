# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 21:26:58 2016

@author: ngundotra
"""
import random
import numpy as np
import matplotlib.pyplot as plt
rule = 90

RULES = ["111", "110", "101", "100", "011", "010", "001", "000"]

class Generate():
    
    """ Converts rule to binary string representation """
    def convertRule(self):
        num = self.rule
        actualRule = ""
        for i in [2**x for x in range(7,-1,-1)]:
            if num - i >= 0:
                actualRule = actualRule + "1"
                num = num - i
            else:
                actualRule = actualRule + "0"
        self.stringRule = actualRule
        self.ruleTable = {RULES[x]:self.stringRule[x] for x in range(8)}
        
    """ Given a decimal rule, and rows and iterations,
    start figuring out the correct cellular automaton"""
    def __init__(self,rule=90, rows=10,iterations=10):
        self.rows = rows
        self.iterations = iterations
        self.rule = rule
        self.matHistory = np.array(dtype=list)
        self.convertRule()
    
    """Generates history of timesteps for self.iterations"""
    def generateString(self,ic=""):
        if len(ic) == 0:
            for x in range(self.rows):
                ic = ic + str(random.randint(0,1))
        self.history = []
        for i in range(self.iterations):
            ic = self.makeFutureString(ic)
            self.history.append(ic)
        self.dump()
        
        
    """Makes subsequent string timestep"""
    def makeFutureString(self, row):
        newLine = ""
        for center in range(len(row)):
            sub = ""
            for adjacent in range(-1,2):
                index = center+adjacent
                if index >= len(row):
                    index = 0
                if row[index] == "1":
                    sub = sub + "1"
                else:
                    sub = sub + "0"
            newLine = newLine + self.ruleTable[sub]
        return newLine
        
    def dump(self):
        f = open("ngundotraCell.txt", "w+")
        for i in self.history:
            f.write(i+"\n")
        f.close()
    
            
rule90 = Generate(iterations=25,rule=101)    
rule90.generateString("0000000001000000000")

#fig, ax = plt.subplots()
#mat = ax.matshow(rule90.history)
    
        
        