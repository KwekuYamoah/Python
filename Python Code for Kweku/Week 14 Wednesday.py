# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:49:55 2019

@author: Kweku Andoh
"""

def main():
        n= int(input("Enter a number which you wnat to find the range of prime numbers for:\n"))
        prime_list=[]
        new_list=[]
        for i in range(2,n+1):
            prime_list.append(i)
        while prime_list != []:
            
            new_list.append(prime_list[0])
            
            for i in prime_list:
                if i % prime_list[0] == 0:
                    prime_list.remove(i)
        print(new_list)
            
                
main()               