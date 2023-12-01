# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:34:45 2023

@author: kenet
"""

urlStr = ""

data = open(urlStr, "r")
output = 0
numbers = ["one","two","three","four","five","six","seven","eight","nine"]

for x in data:
    lofx = len(x)
    first = 0
    last = 0
   
    
    while last == 0:
        temp = 0
        for e in x:
            if last == 1:
                temp = 0
                break
            pos = lofx - temp
            temp += 1
            for n in range(1,10):
                 s = str(n)
                 if x.count(s,pos-1,pos) >= 1:
                     output += n
                     last = 1
                    ## print(n,"l")                     
                     break
                 """ für aufgabe 2 """
                 # if x.count(numbers[n-1],pos-len(numbers[n-1]),lofx) >= 1:
                 #     output += n
                 #     last = 1  
                 #    ## print(n,"l")
                 #     break
                     

    
    while first == 0:
        for c in x:
            if first == 1:
                break
            pos = 0 + temp 
            temp += 1
            for n in range(1,10):
                s = str(n)
                if c.count( s ) >= 1:
                    output += n*10
                    first = 1
                   ## print(n,"f")
                    break
                """ für aufgabe 2 """
                # if x.count(numbers[n-1],pos,pos+len(numbers[n-1])) >= 1:
                #      output += n*10
                #      first = 1 
                #     ## print(n,"f")
                #      break
 
    
 

    
 
    print(output)