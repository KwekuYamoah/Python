# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:32:37 2019

@author: Kweku Andoh Yamoah and Akua Dapaah
"""

class Admission:
    def __init__(self):
        self.admit=[]
    
    def admmit(self,student):
        self.admit.append(student)
        
    def prints(self):
        for i in self.admit:
            print(i)
            
class student:
    def __init__(self):
        self.name=""
        self.age= ""
        self.gender =""
        self.Id=""
        
    def setname(self,rname):
        self.name= rname
    
    def setage(self,rage):
        self.age= rage
    
    def setgender(self,rgender):
        self.gender= rgender
    
    def setId(self,rId):
        self.Id=rId
        
            
def main():
    ashesi= Admission()
    print("Admitting 3 students")
    for i in range(3):
        name = input("Enter your name:\n")
        age= input("Enter your age:\n")
        gender= input("Are you male or female?:\n")
        Id = int(input("Enter your id number:\n"))
        Akua= student()
        Akua.setname(name)
        Akua.setgender(gender)
        Akua.setage(age)
        Akua.setId(Id)
        ashesi.admmit(Akua)
    ashesi.prints()  
         
main()
           

        
    
        