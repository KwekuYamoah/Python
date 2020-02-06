# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''def main():
    
    i = str(input("Enter a number, if you want end just hit enter key to exit:\n"))
    new= []
    while i != "":
        a = int(i)
        new.append(a)
        i = str(input("Enter a number, enter a negative number to exit:\n"))
    print(new) '''
#main()
from math import sqrt
class myMath:
    def __init__(self):
        self.list= []
        
    def getNumbers(self):
        
        i = str(input("Enter a number, if you want end just hit enter key to exit:\n"))
        new= self.list
        while i != "":
            a = int(i)
            new.append(a)
            i = str(input("Enter a number, enter a negative number to exit:\n"))
        return new
    def getMean(self):
        list_num  = self.getNumbers()
        count = 0
        total=0
        for i in list_num:
            total+= i
            count+=1
        mean= total/count
        return mean
    
    
    def getStandardDev(self):
        list_mean= self.getNumbers()
        mean= self.getMean()
        stan = 0
        for i in list_mean:
            stan+= abs(i - mean)
            n= len(list_mean)
        stanDev= sqrt(stan**2/n)
        return stanDev
    
    
    def getMeanandStandardDev(self):
        list_stan=self.getNumbers()
        count = 0
        total=0
        stotal = 0
        for i in list_stan:
            total+= i
            count+=1
            tmean= total/count
            stotal = (abs(i-tmean))
            tstand = sqrt(stotal/count)
        return tmean,tstand
    
    def getMin(self):
        list_min= self.getNumbers()
        minlist = min(list_min)
        return minlist
    
    def getMax(self):
        list_max= self.getNumbers()
        maxlist= max(list_max)
        return maxlist
    
    
kay = myMath()

kay.getNumbers()
    
    
    
    
        
        
        
        
            
        
        
        
            
    
        
        

