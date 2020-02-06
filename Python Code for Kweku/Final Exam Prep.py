# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:31:09 2019

@author: Kweku Yamoah
"""

'''print("Hello, world!")
print("Hello", "world!")
print(3)
print(3.0)
print(2+3)
print(2. +3.0)
print("2+3=", 2+3)
print(7/3)
print(7//3)'''


'''def main():
    print("This program illustrates a chaotic function") 
    x = eval(input("Enter a number between 0 and 1: ")) 
    n= eval(input("Enter a number between 0 and 1:"))
    print("Input","{0:8.2f} {1:15.2f}".format(x,n) )
    print("-------------------------------")
    for i in range(10): 
        x  = 3.9 * x *(1-x)
        n  = 3.9 * n *(1-n)
        
        print("     ","{0:5.7f} {1:15.7f}".format(x,n)) 
main()'''

def main(): 
    print("This is a simple program to convert tempreatures"
          "in degree celsius to degree farenheit")
    print("{0:1} {1:10}".format("Celsius","    Fahrenheit"))
    for temp in range(0,101,10):
        #celsius = eval(input("What is the Celsius temperature? ")) 
        fahrenheit = 9/5 * temp + 32
        
        print("{0:1d} {1:15.2f}".format(temp,fahrenheit)) 
#main() 
    
def main(): 
    print("This program computes the average of three exam scores.") 
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average) 
#main()
    
def main(): 
    print("This program calculates the future value")
    print("of a 10-year investment.") 
    
    years = int(input("Enter the number of years you would like to invest:"))
    for i in range(years):
        principal = eval(input("Enter the initial principal: "))
        apr = eval(input("Enter the annual interest rate: "))
    principal = principal * (1 + apr) 
    print("The value in ", years, " years is:", principal) 
        
#main()
    
def calc():
    print("this is a simple calculator program")
    expr = (input("Enter your mathematical expression:"))
    while expr != "":
        print(eval(expr))
        expr = eval(input("Enter your mathematical expression:"))
#calc()
     
import math 
from math import *
def sphere():
    r = eval(input("Enter the radius of your sphere:"))
    area = 4 * pi * r ** 2
    vol = 4 / 3 * pi * r ** 3
    print("Volume : ",vol, " Area: ",area )
    
#sphere()
    
def pizCost():
    d = eval(input("Diameter of pizza:"))
    c = eval(input("Cost of pizza:"))
    area = pi * d ** 2 / 4
    areaInch = area/c
    print("Cost per square inch of pizza :", areaInch)
#pizCost()

def molWeight():
    h = int(input("Number of hydrogen atoms:"))
    c = int(input("Number of carbon atoms:"))
    o = int(input("Number of oxygen atoms:"))
    weight = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
    print("Molecular weight of carbohydrate:", weight)
    
#molWeight()
    
def litDistance():
    t = eval(input("Enter the time elapse of strike:"))
    dis = 1100 * t
    mile = dis/ 5280
    print("The distance of the lightening strike is ", mile, " miles")
#litDistance()
    
def ship():
    ord_weight = eval(input("Enter the weight of your order in pounds:"))
    cost = (10.50 * ord_weight) + (0.86 + ord_weight) + 1.50
    print("Order cost:", cost)
#ship()
    
def grad():
    x1 , x2 = eval(input("Enter the x coordinates of your two pionts seperated by a comma:"))
    y1, y2 = eval(input("Enter the y coordinates of your two pionts seperated by a comma:"))
    m = (y2 - y1) / (x2 -x1)
    print("Gradient:", round(abs(m),2))
#grad()
    
def distance():
    x1 , x2 = eval(input("Enter the x coordinates of your two pionts seperated by a comma:"))
    y1, y2 = eval(input("Enter the y coordinates of your two pionts seperated by a comma:"))
    m = sqrt((x2- x1) ** 2 + (y2 - y1) ** 2)
    print("Distance:", round(abs(m),2))
#distance()
    
def triangle():
    a,b,c = eval(input("Enter the length of 3 sides sperated by a comma:"))
    s = a + b + c / 2
    area = sqrt(s * (s-a) * (s-b) * (s - c))
    print("triangular area:", round(area,2))
#triangle()
    
def ladder():
    angle = float(input("Enter the angle of inclination in degrees:"))
    height = float(input("Enter the height of the wall:"))
    rad = pi / 180 * angle
    length = height / sin(rad)
    print("lenght of ladder needed is:", length )
#ladder()
    
def cubeSum():
    n = eval(input("Enter the number you want to find sum:"))
    c_sum = (n *(n + 1) / 2) ** 2
    print("Cube Sum:", c_sum)
#cubeSum()
    
def suM():
    n = int(input("How many numbers are you summing?"))
    n_sum = 0
    for i in range(n):
        num = eval(input("Enter number:"))
        n_sum += num
    print(n_sum)
#suM()

def avg_suM():
    n = int(input("How many numbers are you summing?"))
    n_sum = 0
    for i in range(n):
        num = eval(input("Enter number:"))
        n_sum += num
    avg= n_sum/n
    print(avg)
#avg_suM()
    
def pi():
    n = int(input("Number of terms:"))
    raw = 0
    for i in range(n + 1):
        if i % 2 == 0:
            raw += (4/ (2 * i + 1))
        else: 
            raw += -(4/ (2 * i + 1))
    print(raw)
#pi()

def fib():
    n = int(input("Number of terms:"))
    first = 1
    second = 1
    '''fib_value = 0'''
    for i in range(1,n + 1):
        if i == 1 or i == 2:
            fib_value = 1
        else:
            fib_value = first + second
            first = second
            second = fib_value
            
    print(fib_value)
#fib()

def sqr():
    num = int(input("Enter a number:"))
    n = int(input("How many guesses:"))
    init = num/2
    for i in range(n):
        appro = (init + num / init) / 2
        init = appro
    print("Approximate value:",appro)
    print("Error:", sqrt(num) - appro)
    
#sqr()
    
def score():
    quiz = eval(input("Enter your score in the quiz:"))
    if quiz <= 1:
        print("Grade F")
    elif quiz > 1 and quiz <= 2:
        print("Grade D")
    elif quiz > 2 and quiz <=3:
        print("Grade C")
    elif quiz > 3 and quiz <= 4:
        print("grade B")
    elif quiz > 4 and quiz <= 5:
        print("Grade A")
    else:
        print("Out of bounds")
#score()
        

def exam():
    score = eval(input("Score:"))
    if score < 60:
        print("F")
    elif score  >= 60 and score <= 69:
        print("D")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 90 and score <= 100:
        print("A")
    else:
        print("Out of bounds")
#exam()
    
def acronym():
    acro = str(input("Enter phrase:")).split()
    toli= ""
    for word in acro:
        toli += word[0]
    print("Acronym:",toli.upper())
#acronym()

def nameValue():
    name= str(input("Name:")).lower().split()
    print(name)
    slots = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    value = 0
    for letter in name:
        for alpha in letter:
            value += slots.index(alpha) + 1
    print("Name value:",value)
#nameValue()
        
def ceaser():
    word = str(input("Enter plaintext:"))
    key =int(input("Key:"))
    encoded=""
    for alpha in word:
        encoded += chr(ord(alpha) + key)
    print("Encoded:",encoded)
#ceaser()

def circceaser():
    word = str(input("Enter plaintext:")).lower().split()
    key =int(input("Key:"))
    slots = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    en_slots =[]
    new =[]
    encoded = ""
    while slots != []:
        en_slots.append(slots[-1])
        slots.remove(slots[-1])
    for alpha in word:
        for le in alpha:
            encoded += chr(en_slots.index(le) + key)
        new.append(encoded)
    print(new)
        
        
#circceaser()
    
def countWords():
    sen =str(input("Sentence:"))
    len_sen= len(sen)
    sen = sen.split()
    count = 0
    for word in sen:
        count +=1
    avg= len_sen/count
    print(avg)  
#countWords() 
    
def main():
    print("This program illustrates a chaotic function") 
    x = eval(input("Enter a number between 0 and 1: ")) 
    n= eval(input("Enter a number between 0 and 1:"))
    print("Input","{0:8.2f} {1:15.2f}".format(x,n) )
    print("------------------------------------")
    for i in range(10):
        x  = 3.9 * x *(1-x)
        n  = 3.9 * n *(1-n)
        
        print("{0:^5}{1:^15.7f} {2:^20.7f}".format(i,x,n)) 
#main()
        
def main(): 
    print("This program calculates the future value")
    print("of a 10-year investment.") 
    principal = eval(input("Enter the amount of investment:"))
    apr = eval(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years you would like to invest:"))
    print("{0:5^} {1:^10}".format("Year","Value"))
    print("---------------")
    for i in range(years):
        principal = principal * (1 + apr)
        print("{0:^5} {1:^10.2f}".format(i,principal))
     
        
#main()
        
def wc():
    infile= open("Final.txt","r").readlines()
    lines = 0
    count = 0
    for line in infile:
        lines +=1
        for word in line.split():
            word = word.rstrip("\n")
            count += 1
    print("lines:",lines," Words:", count)
    
    infile= open("Final.txt","r").read()
    print("characters:",len(infile))
#wc()
import math 
from math import *
def sphereArea(radius):
    area = 4 * pi * radius ** 2
    return area

def sphereVolume(radius):
    vol = 4 / 3 * pi * radius ** 3
    return vol

def main():
    r = eval(input("Radius:"))
    surf_area = sphereArea(r)
    volume = sphereVolume(r)
    print("Surface Area:", surf_area," Volume:",volume)
#main()
    
def sumN(n):
    return ((n * (n+1))/2)
def sumNcubes(n):
    return ((n * (n+1))/2) ** 2
def main():
    terms = eval(input("Enter the nth term:"))
    print("Sum of ", terms, " natural numbers:",sumN(terms),
          "Sum of the cube", terms, " natural numbers:",sumNcubes(terms))
#main()
    
def squareEach(nums):
    new=[]
    for i in nums:
        new.append(i ** 2)
    return new

def main():
    inp= eval(input("Enter numbers seprated by comma:"))
    ist =list(inp)
    print("Square of array is :", squareEach(ist))  
#main()
    
def sumList(nums):
    new=0
    for i in nums:
        new += i
    return new

def main():
    inp= eval(input("Enter numbers seprated by comma:"))
    ist =list(inp)
    print("Sum of array is :", sumList(ist))  
#main()
    
def toNumbers(strLists):
    new=[]
    for i in strLists:
        new.append(int(i) ** 2)
    return new

def main():
    inp= eval(input("Enter numbers as strings seprated by comma:"))
    ist =list(inp)
    print("numbers of array is :", toNumbers(ist))  
#main()
    
def squareEach(nums):
    infile = open(nums,"r")
    new=[]
    for i in infile:
        new.append(int(i) ** 2)
    return new

def main():
    file = input("Enter name of file:")
    print("Square of array is :", squareEach(file))  
#main()

def wage(rate,hrs):
    if hrs <= 40:
        wage = rate * hrs 
    else:
        wage = 40 * rate +(((hrs - 40)* rate) *1.5)
    return wage
def main():
    hours = eval(input("Enter hours worked, eg. 8.5:"))
    pay = eval(input("Enter pay rate, eg, 1.80:"))
    print("Wage:",wage(pay,hours))
#main()

def bmi(w,h):
    bmi= w *720/ h ** 2
    if 19 <= bmi <= 25:
        print("You are healthy")
    elif bmi > 25:
        print("Hey!!, you need to hit the gym")
    else:
        print("You need some calories")
    return bmi
        
def main():
    weight = eval(input("Enter weight in pounds:"))
    height = eval(input("Height in inches:"))
    print("Your BMI:",bmi(weight,height))
#main()
    
def sitter(start,end):
    hr , mins= start.split(":")
    e_hr,e_mins = end.split(":")
    e_hrn,e_min = int(e_hr),int(e_mins)
    hrn,smins= int(hr), int(mins)
    
    
    if hrn <= 21:
        wage = 2.5 * (e_hrn - hrn) + 2.5 * (e_min - smins)/60
    else:
        wage = 2.5 * (21 - hrn ) +((e_hrn - 21 * 1.5) + e_min/60 * 1.5) + smins/60 * 2.5
        
    return wage


def main():
    s_time = str(input("Enter start time, eg. 8:00:" ))
    e_time = str(input("Enter end time, eg. 8:00:" ))
    print("Pay:", sitter(s_time,e_time))

def us(age,c_year):
    if age >= 30 and c_year >= 9:
        print("Eligible for senator")
    elif age >= 27 and c_year >= 7:
        print("Eligible for Us representative")
    else:
        print("Not Eligible")
def main():
    age, years = eval(input("Enter age and years of citizenship seperated by a comma:  "))
    us(age,years)
#main()
    
def easter():
    year = eval(input("Enter a year:"))
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = ( 19 * a + 24) % 30
        e = (2* b + 4 * c + 6 * d + 5) % 7
        print("Easter is: March 22",d , e)
    else:
        print("Out of range")
#easter()
        
def leap():
    print("Welcome to the leap year verifier")
    print("-" * 35)

    year= int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            print("Leap Year!!")
    else:
        print("Sorry, not a leap year")
#leap()
        
def dateVal():
    da = str(input("Enter a year in the format m/d/y: ")).split("/")
    month,day,year=da
    if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) <= 30:
            print("Date is Valid")
        else:
            print("Date not Valid")
    elif int(month) == 2:
        if int(day) <= 29:
            print("Date is Valid")
        else:
            print("Date is not Valid")
    else:
        if int(day) <= 31:
            print("Valid date ")
        else:
            print("Date not Valid")
dateVal()