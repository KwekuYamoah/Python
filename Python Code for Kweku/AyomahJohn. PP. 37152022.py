# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:11:24 2018

@author: John Ayomah
"""
def venom():
    balance = eval(input("Enter your expected balance in cedis, if balance is in pesewas enter balance in balance/100 \n"))
    denomination = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1,]
    bringBack = []
    for a in denomination:
        while balance >=a:
            bringBack.append(a)
            balance = balance - a
    print("Pay customer " + str(bringBack) + " notes")
    
    
    
venom()