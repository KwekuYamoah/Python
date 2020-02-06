# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 07:06:48 2019

@author: Kweku Yamoah
"""

from math import *
def earthdist(t1,g1,t2,g2):
    dist = 6371.01 * acos((sin(t1) * sin(t2) + (cos(t1) * cos(t2) * cos(g1 - g2))))
    return dist

def main():
    long1, lad1 = eval(input("Enter the longitude and latitude in degrees for your first point,seperated by a comma:\n"))
    rlong1 = radians(long1)
    rlad1 = radians(lad1)
    long2, lad2 = eval(input("Enter the longitude and latitude in degrees for your second point,seperated by a comma \n"))
    rlong2 = radians(long2)
    rlad2 = radians(lad2)
    distance = earthdist(rlong1,rlad1,rlong2,rlad2)
    print(distance)
    
#main()
    
def height():
    ft, inch = eval(input("Enter your height in feets, followed by your height in inches,"
                     "seperated by a comma:\n"))
    calcInch = ft * 12
    calcCenti = calcInch * 2.54
    inchCenti = inch * 2.54
    print("Your height in feet in inches is,","", round(calcInch,2),"", "and in centimeters is","", round(calcCenti,2))
    print("Your height in inches in centimetres is","",round(inchCenti,2))
    
    
#height()
    
def capacity():
    temp1, temp2 = eval(input("Enter the initial tempreature and the final tempreature seperated by a comma,:\n"))
    mass = eval(input("Enter the mass of th water in grams:\n"))
    quant = 4.186 * mass * (temp2 -temp1)
    kiloW = quant * 2.777778 * 10 ** -7
    heat = (kiloW * 8.9)
    print("The heat capacity of the object is,", quant)
    print("The cost of heating the water is,", heat,"dollars")
    
capacity()
