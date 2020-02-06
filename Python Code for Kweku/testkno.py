# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:11:18 2019

@author: User
"""

'''def main():
    s_limit= eval(input("Enter the speed limit:\n"))
    d_speed= eval(input("Enter the driving speed:\n"))
    if d_speed == s_limit:
        fine= 50
        print(str(fine))
    elif d_speed > s_limit:
        if d_speed <= 145:
            fine = 50 + (d_speed- s_limit) *5
            print(str(fine))
        else:
            fine = 50 + (d_speed- s_limit) *5 + 200
            print(str(fine))
    else:
        print("Within limit")
        
main()'''


a = [1,2,3,4]
b = [2,3,4,5]
ab = []                        
for i in range(0, len(a)):
     ab.append(a[i]*b[i]) 
     
print(ab)