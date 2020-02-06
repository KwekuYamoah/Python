# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:03:52 2019

@author: Kweku Andoh Yamoah(71712022)
"""

def main():
    printIntro()
    list1, list2= getInput()
    prod_list= innerProd(list1, list2)
    printResults(list1,list2,prod_list)
    
    
def printIntro():
    print("This is a simple program to calculate the inner product of two list\n")
    print("The product is gotten by take equal indexes of the elements in the corresponding lists and multiplying them as x and y values\n")
    print("The results is printed out neatly in a formatted table\n")
    print("Caution, for the code to run, the list should be of equal length\n")
    
    
def getInput():
    list1= str(input("Enter the items of your first list seprated by a comma :\n")).split(",")
    list2= str(input("Enter the items of your sperated list seprated by a comma :\n")).split(",")
        
    return list1,list2
    


def innerProd(list1,list2):
    int_list1 =[]
    int_list2 = []
    for i in list1:
        int_list1.append(int(i))
    
    for j in list2:
        int_list2.append(int(j))
    
    
    prod_list=[]
    for i in range(0,len(int_list1)):
         prod_list.append((int_list1[i]) * (int_list2[i]))
    return prod_list
    
    
def printResults(list1,list2,prod_list):
        print("The inner products of the elemenst of the list are:\n")
        print(prod_list,end="")
    
    
main()
    
    
    
    
    
    
    



    