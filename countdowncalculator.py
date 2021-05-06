# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:16:50 2021

@author: Team Knowhow
"""
targetnum = float(input("type number to achieve: "))
signs = input("type operations: ")

a = 1
225
b= len(signs)

import itertools 

onetonine = [1,2,3,4,5,6,7,8,9]

def operationsfunct(num1, num2, op):
    if op =="+":
        b = (num1 + num2)
    
    elif op == "-":
        b = (num1 - num2)
    
    elif op == "/":
        b = (num1 / num2)
    
    elif op == "*":
        b = (num1 * num2)
    
    else: 
        b = ("N/A")
        
    return b    

result = list(itertools.permutations(onetonine,len(signs)+1))

#print(result)
num1 = result[0][0]
num2 = result[0][1]
target = 1
listnum = 0

while target != targetnum:
    
    for i in range(len(signs)):
        num2 = float(result[listnum][i+1])
        prt1 = operationsfunct(num1, num2, signs[i])        
        num1 = prt1
    target = prt1    
    # if listnum == 498:
    #     sleep(60)
    # else:
    #     listnum = listnum
    listnum = listnum +1
    
    num1 = float(result[listnum][0])
    num2 = float(result[listnum][0])
    
print(target)
print(result[listnum-1])    

