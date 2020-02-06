# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:37:54 2019

@author: Kweku Andoh Yamoah
"""

class methods:
    def __init__(self,myList):
        self.Count= myList
        self.Isin=myList
        self.Index=myList
        self.Reverse=myList
        self.Sort=myList
        
    def getCount(self,x):
        count=0
        for i in self.Count:
            if x == i:
                count += 1
                return count
            else:
                return None
            
    def getIsin(self,x):
        is_in= bool(0)
        for i in self.Isin:
            if i == x:
                is_in= bool(1)
                
        return is_in
        
    
    def getIndex(self,x):
        for i in range(len(self.Index)):
            if self.Index[i] == x:
                return i
            
            
            
    def getReverse(self):
        rev= self.Reverse
        return rev[-1::-1]
    
    
    def getSort(self):
        new= self.Sort
        sortList=[]
        while new != []:
            value= new[0]
            for i in new:
                if i < value:
                    value= i
            sortList.append(value)
            new.remove(value)
        return sortList
    
    
    
    
test = methods([2,3,4,5,6,7,8,9,3,6,4,5,6,9,1,2,4])
print(test.getCount(2))
print(test.getIsin(2))
print(test.getIndex(2))
print(test.getReverse())
print(test.getSort())
        
            
        